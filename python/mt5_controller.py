"""
MT5 Controller
Designed by Serkan

Bu modül, MetaTrader 5 ile tüm teknik etkileşimi yönetir.
- Bağlantı
- Login
- Sembol bilgisi
- Fiyat verisi
- İşlem açma / kapama

Bu katman:
- Doğrudan AI ile konuşmaz
- Sadece teknik MT5 operasyonlarını yürütür
- Üst katmanlardan (orchestrator vb.) gelen komutları uygular
"""

from typing import Optional, Dict, Any

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None


class MT5Controller:
    def __init__(
        self,
        logger=None,
        safety_engine=None,
        server: Optional[str] = None,
        login: Optional[int] = None,
        password: Optional[str] = None
    ):
        """
        MT5 Controller başlangıç.

        :param logger: Dışarıdan verilen logging engine (opsiyonel)
        :param safety_engine: Güvenlik ve risk kontrol katmanı (opsiyonel)
        :param server: MT5 sunucu adı
        :param login: MT5 hesap numarası
        :param password: MT5 şifre
        """
        self.logger = logger
        self.safety_engine = safety_engine
        self.server = server
        self.login = login
        self.password = password
        self.connected = False

        if mt5 is None:
            self._log_error("MetaTrader5 modülü bulunamadı. MT5 fonksiyonları devre dışı.")
        else:
            self._log_info("MT5Controller hazır. Bağlantı henüz kurulmadı.")

    # -------------------------------------------------------------------------
    # Yardımcı log fonksiyonları
    # -------------------------------------------------------------------------
    def _log_info(self, msg: str):
        if self.logger:
            self.logger.info(f"[MT5Controller] {msg}")
        else:
            print(f"[MT5Controller][INFO] {msg}")

    def _log_error(self, msg: str):
        if self.logger:
            self.logger.error(f"[MT5Controller] {msg}")
        else:
            print(f"[MT5Controller][ERROR] {msg}")

    # -------------------------------------------------------------------------
    # Bağlantı yönetimi
    # -------------------------------------------------------------------------
    def initialize(self) -> bool:
        """
        MT5 terminalini başlatır ve login olmaya hazırlar.
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, initialize başarısız.")
            return False

        if not mt5.initialize():
            self._log_error(f"MT5 initialize başarısız: {mt5.last_error()}")
            return False

        self._log_info("MT5 initialize başarılı.")
        return True

    def login_account(self) -> bool:
        """
        MT5 hesabına login olur.
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, login yapılamaz.")
            return False

        if self.login is None or self.password is None or self.server is None:
            self._log_error("Login bilgileri eksik (login / password / server).")
            return False

        authorized = mt5.login(self.login, password=self.password, server=self.server)
        if not authorized:
            self._log_error(f"MT5 login başarısız: {mt5.last_error()}")
            self.connected = False
            return False

        self.connected = True
        self._log_info(f"MT5 login başarılı. Hesap: {self.login}")
        return True

    def is_connected(self) -> bool:
        """
        MT5 bağlantı durumunu döner.
        """
        return self.connected

    def shutdown(self):
        """
        MT5 bağlantısını kapatır.
        """
        if mt5 is not None:
            mt5.shutdown()
        self.connected = False
        self._log_info("MT5 bağlantısı kapatıldı.")

    # -------------------------------------------------------------------------
    # Sembol ve fiyat bilgisi
    # -------------------------------------------------------------------------
    def ensure_symbol(self, symbol: str) -> bool:
        """
        Sembolün MT5 tarafında kullanılabilir olduğundan emin olur.
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, sembol kontrolü yapılamaz.")
            return False

        if not mt5.symbol_select(symbol, True):
            self._log_error(f"Sembol seçilemedi: {symbol}")
            return False

        self._log_info(f"Sembol hazır: {symbol}")
        return True

    def get_tick(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Sembol için son tick verisini döner.
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, tick alınamaz.")
            return None

        if not self.ensure_symbol(symbol):
            return None

        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            self._log_error(f"Tick verisi alınamadı: {symbol}")
            return None

        return {
            "symbol": symbol,
            "bid": tick.bid,
            "ask": tick.ask,
            "last": tick.last,
            "time": tick.time
        }

    # -------------------------------------------------------------------------
    # İşlem açma / kapama
    # -------------------------------------------------------------------------
    def open_position(
        self,
        symbol: str,
        action: str,
        volume: float,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        comment: str = "AI Trade"
    ) -> Optional[int]:
        """
        Yeni bir pozisyon açar.

        :param symbol: İşlem yapılacak sembol
        :param action: "BUY" veya "SELL"
        :param volume: Lot miktarı
        :param stop_loss: Fiyat seviyesinde SL
        :param take_profit: Fiyat seviyesinde TP
        :param comment: İşlem yorumu
        :return: Ticket numarası veya None
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, işlem açılamaz.")
            return None

        if not self.connected:
            self._log_error("MT5 bağlı değil, işlem açılamaz.")
            return None

        if self.safety_engine:
            if not self.safety_engine.can_open_trade(symbol=symbol, action=action, volume=volume):
                self._log_error("SafetyEngine işlemi reddetti.")
                return None

        if not self.ensure_symbol(symbol):
            return None

        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            self._log_error(f"Tick verisi alınamadı, işlem açılamaz: {symbol}")
            return None

        order_type = mt5.ORDER_TYPE_BUY if action.upper() == "BUY" else mt5.ORDER_TYPE_SELL
        price = tick.ask if action.upper() == "BUY" else tick.bid

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "sl": stop_loss if stop_loss else 0.0,
            "tp": take_profit if take_profit else 0.0,
            "deviation": 10,
            "magic": 123456,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }

        self._log_info(f"İşlem açma isteği: {request}")

        result = mt5.order_send(request)
        if result is None:
            self._log_error("order_send None döndü.")
            return None

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            self._log_error(f"order_send hata: {result.retcode}, {result.comment}")
            return None

        ticket = result.order
        self._log_info(f"İşlem açıldı. Ticket: {ticket}")
        return ticket

    def close_position(self, ticket: int) -> bool:
        """
        Verilen ticket numarasına göre pozisyonu kapatır.
        """
        if mt5 is None:
            self._log_error("MetaTrader5 modülü yok, işlem kapatılamaz.")
            return False

        if not self.connected:
            self._log_error("MT5 bağlı değil, işlem kapatılamaz.")
            return False

        position = mt5.positions_get(ticket=ticket)
        if not position:
            self._log_error(f"Ticket bulunamadı veya açık pozisyon yok: {ticket}")
            return False

        position = position[0]
        symbol = position.symbol
        volume = position.volume
        order_type = position.type

        tick = mt5.symbol_info_tick(symbol)
        if tick is None:
            self._log_error(f"Tick verisi alınamadı, pozisyon kapatılamaz: {symbol}")
            return False

        if order_type == mt5.POSITION_TYPE_BUY:
            price = tick.bid
            close_type = mt5.ORDER_TYPE_SELL
        else:
            price = tick.ask
            close_type = mt5.ORDER_TYPE_BUY

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": close_type,
            "position": ticket,
            "price": price,
            "deviation": 10,
            "magic": 123456,
            "comment": "AI Close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }

        self._log_info(f"Pozisyon kapatma isteği: {request}")

        result = mt5.order_send(request)
        if result is None:
            self._log_error("order_send None döndü (close).")
            return False

        if result.retcode != mt5.TRADE_RETCODE_DONE:
            self._log_error(f"Pozisyon kapatma hata: {result.retcode}, {result.comment}")
            return False

        self._log_info(f"Pozisyon kapatıldı. Ticket: {ticket}")
        return True
