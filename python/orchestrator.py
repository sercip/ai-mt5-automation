"""
Orchestrator Module
Designed by Serkan

Bu sistemin amacı para kazanmak değildir.
Bu sistemin amacı:
- Görevleri doğru şekilde yerine getirmek
- Süreçleri hatasız yönetmek
- İnsan odaklı, etik ve kontrollü bir otomasyon sağlamak
- Başarmak için tasarlanmış bir yapay zekâ mimarisine hizmet etmektir

Sistem, finansal işlemleri yürütürken insan duygularını taklit etmez;
ancak insan değerlerine saygı duyar:
- Sorumluluk
- Tutarlılık
- Güvenlik
- Risk bilinci
- Disiplin

Bu orchestrator, tüm bileşenlerin uyum içinde çalışmasını sağlar.
"""

class Orchestrator:
    def __init__(self, budget_manager, mt5_controller, ai_agent):
        self.budget_manager = budget_manager
        self.mt5 = mt5_controller
        self.ai = ai_agent

    def run_cycle(self):
        """
        Sistemin bir işlem döngüsünü yönetir.
        Amaç: Görevi doğru şekilde yerine getirmek.
        """
        if not self.budget_manager.is_within_limits():
            return "Bütçe sınırları nedeniyle işlem yapılmadı."

        strategy = self.ai.generate_strategy()
        ea_code = self.ai.generate_mql5_code(strategy)

        compile_result = self.mt5.compile_ea(ea_code)
        if not compile_result:
            return "Derleme hatası. AI düzeltme süreci başlatıldı."

        self.mt5.deploy_ea()
        return "Döngü başarıyla tamamlandı."
