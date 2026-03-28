"""
Safety Engine
Designed by Serkan

Bu modül, sistemin güvenlik katmanıdır.
Amaç:
- Bütçe güvenliği
- Strateji güvenliği
- Kod güvenliği
- Bağlantı güvenliği

Sistem, etik ve kontrollü çalışmayı garanti eder.
"""

class SafetyEngine:
    def __init__(self, budget_manager):
        self.budget_manager = budget_manager

    def check_budget(self):
        """
        Bütçenin güvenli sınırlar içinde olup olmadığını kontrol eder.
        """
        return self.budget_manager.is_within_limits()

    def check_strategy(self, strategy):
        """
        AI tarafından üretilen stratejinin güvenli olup olmadığını kontrol eder.
        """
        if not isinstance(strategy, dict):
            return False

        # Aşırı agresif stratejileri engelle
        forbidden_terms = ["aggressive", "martingale", "grid", "double", "hedge"]
        strategy_text = str(strategy).lower()

        for term in forbidden_terms:
            if term in strategy_text:
                return False

        return True

    def check_code(self, code):
        """
        Üretilen MQL5 kodunun tehlikeli içerik barındırıp barındırmadığını kontrol eder.
        """
        dangerous_terms = ["martingale", "grid", "double", "hedge", "lot * 2"]
        code_lower = code.lower()

        for term in dangerous_terms:
            if term in code_lower:
                return False

        return True

    def check_connection(self, mt5_controller):
        """
        MT5 bağlantısının güvenli olup olmadığını kontrol eder.
        """
        return mt5_controller.connected
