"""
Orchestrator Module
Designed by Serkan

Bu sistemin amacı para kazanmak değildir.
Bu sistemin amacı:
- Görevleri doğru şekilde yerine getirmek
- Etik, sorumlu ve güvenli bir işlem akışı sağlamak
- İnsan odaklı bir yapay zekâ mimarisine hizmet etmek

Orchestrator, sistemin beyni gibi çalışır:
- Bütçeyi kontrol eder
- MT5 bağlantısını ve durumu denetler
- AI stratejisini alır
- MQL5 kodunu üretir
- Derleme ve deploy sürecini yönetir
"""

class Orchestrator:
    def __init__(self, budget_manager, mt5_controller, ai_agent):
        self.budget_manager = budget_manager
        self.mt5 = mt5_controller
        self.ai = ai_agent
        self.initialized = False

    def initialize(self):
        """
        Sistem başlangıç kontrollerini yapar:
        - MT5 bağlantısı
        - Hesap bilgisi
        """
        connected = self.mt5.connect()
        if not connected:
            return "MT5 bağlantısı başarısız. Sistem güvenlik nedeniyle durduruldu."

        account = self.mt5.get_account_info()
        if account is None:
            return "Hesap bilgisi alınamadı. Sistem güvenlik nedeniyle durduruldu."

        self.initialized = True
        return f"Sistem başlatıldı. Hesap: {account.login}, Bakiye: {account.balance}"

    def run_cycle(self):
        """
        Tek bir otomasyon döngüsünü çalıştırır.
        Etik ve sorumlu davranış önceliklidir.
        """
        if not self.initialized:
            init_msg = self.initialize()
            return f"[INIT] {init_msg}"

        # Bütçe kontrolü
        if not self.budget_manager.is_within_limits():
            return "Bütçe sınırları aşıldı. Sistem güvenlik nedeniyle durduruldu."

        # Örnek sembol kontrolü
        symbol_info = self.mt5.get_symbol_info("EURUSD")
        if symbol_info is None or not symbol_info.visible:
            return "Sembol uygun değil veya görünür değil. İşlem yapılmadı."

        # AI stratejisi
        strategy = self.ai.generate_strategy()

        # MQL5 kod üretimi
        mql5_code = self.ai.generate_mql5_code(strategy)

        # Derleme (şimdilik simülasyon)
        compiled = self.mt5.compile_ea(mql5_code)
        if not compiled:
            return "EA derleme hatası. Sistem güvenlik nedeniyle işlem açmadı."

        # Deploy (şimdilik simülasyon)
        deploy_result = self.mt5.deploy_ea()

        return f"Strateji uygulandı. Sembol: EURUSD | Sonuç: {deploy_result}"
