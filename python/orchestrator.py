"""
Orchestrator
Designed by Serkan

Bu modül, sistemin beynidir.
Görevleri sırasıyla yönetir:

1) AI'dan strateji alır
2) SafetyEngine'e kontrol ettirir
3) MT5Controller ile işlemi gerçekleştirir
4) LoggingEngine ile her adımı kaydeder

Orchestrator:
- Kural koymaz
- Risk hesaplamaz
- İşlem açmaz
- Strateji üretmez

Sadece tüm katmanları doğru sırayla çalıştırır.
"""

class Orchestrator:
    def __init__(self, ai_agent, mt5_controller, safety_engine, logger):
        """
        :param ai_agent: AIAgentInterface instance
        :param mt5_controller: MT5Controller instance
        :param safety_engine: SafetyEngine instance
        :param logger: LoggingEngine instance
        """
        self.ai_agent = ai_agent
        self.mt5 = mt5_controller
        self.safety = safety_engine
        self.logger = logger

        self.logger.info("[Orchestrator] Sistem başlatıldı.")

    # -------------------------------------------------------------------------
    # Ana çalışma fonksiyonu
    # -------------------------------------------------------------------------
    def run_once(self):
        """
        Sistemin tek bir döngüsünü çalıştırır.
        Bu fonksiyon scheduler veya operator tarafından çağrılır.
        """

        self.logger.info("[Orchestrator] Yeni döngü başlatılıyor...")

        # 1) AI'dan strateji al
        strategy = self.ai_agent.generate_strategy()
        self.logger.info(f"[Orchestrator] AI strateji üretti: {strategy}")

        symbol = strategy.get("symbol")
        action = strategy.get("action")
        confidence = strategy.get("confidence", 0)

        # 2) Safety kontrolü
        if not self.safety.is_strategy_safe(strategy):
            self.logger.warning("[Orchestrator] SafetyEngine stratejiyi reddetti.")
            return False

        self.logger.info("[Orchestrator] SafetyEngine stratejiyi onayladı.")

        # 3) MT5 bağlantı kontrolü
        if not self.mt5.is_connected():
            self.logger.error("[Orchestrator] MT5 bağlı değil, işlem yapılamaz.")
            return False

        # 4) İşlem açma
        volume = self.safety.calculate_safe_lot(symbol, confidence)
        self.logger.info(f"[Orchestrator] Güvenli lot hesaplandı: {volume}")

        ticket = self.mt5.open_position(
            symbol=symbol,
            action=action,
            volume=volume,
            stop_loss=strategy.get("stop_loss"),
            take_profit=strategy.get("take_profit"),
            comment="AI Orchestrator Trade"
        )

        if ticket is None:
            self.logger.error("[Orchestrator] İşlem açılamadı.")
            return False

        self.logger.info(f"[Orchestrator] İşlem açıldı. Ticket: {ticket}")
        return True

    # -------------------------------------------------------------------------
    # MQL5 kod üretimi
    # -------------------------------------------------------------------------
    def generate_mql5(self):
        """
        AI tarafından üretilen stratejiye göre MQL5 kodu oluşturur.
        """
        strategy = self.ai_agent.generate_strategy()
        code = self.ai_agent.generate_mql5_code(strategy)

        self.logger.info("[Orchestrator] MQL5 kodu üretildi.")
        return code

    # -------------------------------------------------------------------------
    # Manuel işlem tetikleme
    # -------------------------------------------------------------------------
    def manual_trade(self, symbol, action, volume):
        """
        Operatör tarafından manuel işlem açmak için kullanılır.
        """
        self.logger.info(f"[Orchestrator] Manuel işlem isteği: {symbol}, {action}, {volume}")

        if not self.safety.can_open_trade(symbol, action, volume):
            self.logger.warning("[Orchestrator] SafetyEngine manuel işlemi reddetti.")
            return False

        ticket = self.mt5.open_position(symbol, action, volume)
        if ticket:
            self.logger.info(f"[Orchestrator] Manuel işlem açıldı. Ticket: {ticket}")
            return True

        self.logger.error("[Orchestrator] Manuel işlem açılamadı.")
        return False
