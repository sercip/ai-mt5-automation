"""
Operator Client
Designed by Serkan

Bu modül, operatörün sistemle güvenli şekilde etkileşime geçmesini sağlar.
Görevleri:
- Manuel işlem açma isteği oluşturmak
- Manuel işlem kapatma isteği oluşturmak
- AI stratejisini görüntülemek
- Logları okumak
- Sistem durumunu sorgulamak

Operator Client:
- MT5'e doğrudan komut göndermez
- İşlem açmaz
- Sadece Orchestrator'a istek iletir
"""

class OperatorClient:
    def __init__(self, orchestrator, logger=None):
        self.orchestrator = orchestrator
        self.logger = logger

        if self.logger:
            self.logger.info("[OperatorClient] Operatör arayüzü başlatıldı.")

    # -------------------------------------------------------------------------
    # Manuel işlem açma isteği
    # -------------------------------------------------------------------------
    def request_open_trade(self, symbol: str, action: str, volume: float):
        """
        Operatör manuel işlem açmak istediğinde çağrılır.
        Orchestrator'a iletilir.
        """
        if self.logger:
            self.logger.info(
                f"[OperatorClient] Manuel işlem isteği: {symbol} {action} {volume}"
            )

        return self.orchestrator.handle_manual_trade_request(
            symbol=symbol,
            action=action,
            volume=volume
        )

    # -------------------------------------------------------------------------
    # Manuel işlem kapatma isteği
    # -------------------------------------------------------------------------
    def request_close_all(self):
        """
        Tüm açık işlemleri kapatma isteği.
        """
        if self.logger:
            self.logger.info("[OperatorClient] Tüm işlemleri kapatma isteği gönderildi.")

        return self.orchestrator.close_all_positions()

    # -------------------------------------------------------------------------
    # AI stratejisini görüntüleme
    # -------------------------------------------------------------------------
    def preview_ai_strategy(self):
        """
        AI'nın üreteceği stratejiyi önizleme.
        """
        strategy = self.orchestrator.ai.generate_strategy()

        if self.logger:
            self.logger.info(f"[OperatorClient] AI strateji önizleme: {strategy}")

        return strategy

    # -------------------------------------------------------------------------
    # Log okuma
    # -------------------------------------------------------------------------
    def read_logs(self, limit=20):
        """
        Son X satır logu okur.
        """
        try:
            with open("logs/system.log", "r", encoding="utf-8") as f:
                lines = f.readlines()
                return lines[-limit:]
        except FileNotFoundError:
            return ["Log dosyası bulunamadı."]

    # -------------------------------------------------------------------------
    # Sistem durumunu sorgulama
    # -------------------------------------------------------------------------
    def system_status(self):
        """
        Sistemin genel durumunu döner.
        """
        status = {
            "ai_loaded": self.orchestrator.ai.model_loaded,
            "mt5_connected": self.orchestrator.mt5.is_connected,
            "safety_active": True,
            "log_active": True
        }

        if self.logger:
            self.logger.info(f"[OperatorClient] Sistem durumu: {status}")

        return status
