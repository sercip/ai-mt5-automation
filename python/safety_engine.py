"""
Safety Engine
Designed by Serkan

Bu modül, sistemin güvenlik ve risk kontrol katmanıdır.
Görevleri:
- AI stratejisini doğrulamak
- Risk limitlerini uygulamak
- Lot miktarını güvenli seviyeye dönüştürmek
- Yasaklı sembolleri engellemek
- Aşırı güven (confidence) durumlarını dengelemek

Safety Engine:
- İşlem açmaz
- Strateji üretmez
- MT5'e doğrudan komut göndermez
"""

class SafetyEngine:
    def __init__(self, logger=None):
        self.logger = logger

        # Temel risk parametreleri
        self.max_lot = 0.10
        self.min_lot = 0.01
        self.max_confidence = 0.95
        self.min_confidence = 0.10

        # Yasaklı semboller (örnek)
        self.blocked_symbols = ["BTCUSD", "XAUJPY"]

        if self.logger:
            self.logger.info("[SafetyEngine] Güvenlik sistemi başlatıldı.")

    # -------------------------------------------------------------------------
    # Strateji güvenlik kontrolü
    # -------------------------------------------------------------------------
    def is_strategy_safe(self, strategy: dict) -> bool:
        """
        AI tarafından üretilen stratejiyi kontrol eder.
        """
        symbol = strategy.get("symbol")
        action = strategy.get("action")
        confidence = strategy.get("confidence", 0)

        # Yasaklı sembol kontrolü
        if symbol in self.blocked_symbols:
            self._log(f"Yasaklı sembol reddedildi: {symbol}")
            return False

        # Confidence kontrolü
        if confidence > self.max_confidence:
            self._log(f"Confidence çok yüksek ({confidence}), reddedildi.")
            return False

        if confidence < self.min_confidence:
            self._log(f"Confidence çok düşük ({confidence}), reddedildi.")
            return False

        # Action kontrolü
        if action not in ["BUY", "SELL"]:
            self._log(f"Geçersiz işlem yönü: {action}")
            return False

        self._log("Strateji güvenli bulundu.")
        return True

    # -------------------------------------------------------------------------
    # Lot hesaplama
    # -------------------------------------------------------------------------
    def calculate_safe_lot(self, symbol: str, confidence: float) -> float:
        """
        Confidence değerine göre güvenli lot hesaplar.
        """
        # Confidence 0.1 → min_lot
        # Confidence 0.95 → max_lot

        scaled = self.min_lot + (self.max_lot - self.min_lot) * confidence

        # Limitlere göre kes
        safe_lot = max(self.min_lot, min(self.max_lot, scaled))

        self._log(f"Güvenli lot hesaplandı: {safe_lot}")
        return round(safe_lot, 2)

    # -------------------------------------------------------------------------
    # Manuel işlem güvenlik kontrolü
    # -------------------------------------------------------------------------
    def can_open_trade(self, symbol: str, action: str, volume: float) -> bool:
        """
        Operatör tarafından manuel işlem açılırken güvenlik kontrolü.
        """
        if symbol in self.blocked_symbols:
            self._log(f"Manuel işlem reddedildi (yasaklı sembol): {symbol}")
            return False

        if action not in ["BUY", "SELL"]:
            self._log(f"Manuel işlem reddedildi (geçersiz yön): {action}")
            return False

        if volume < self.min_lot or volume > self.max_lot:
            self._log(f"Manuel işlem reddedildi (lot sınırı): {volume}")
            return False

        self._log("Manuel işlem güvenli.")
        return True

    # -------------------------------------------------------------------------
    # Log helper
    # -------------------------------------------------------------------------
    def _log(self, msg: str):
        if self.logger:
            self.logger.info(f"[SafetyEngine] {msg}")
        else:
            print(f"[SafetyEngine] {msg}")
