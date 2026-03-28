"""
Budget Manager Module
Designed by Serkan

Bu sistemin amacı para kazanmak değildir.
Bu sistemin amacı:
- Bütçeyi korumak
- Riskleri kontrol altında tutmak
- Sorumlu, etik ve güvenli bir işlem ortamı sağlamak
- İnsan odaklı bir yapay zekâ mimarisine hizmet etmek

Sistem, finansal kararlar alırken insan duygularını taklit etmez;
ancak insan değerlerini temel alır:
- Aşırı riskten kaçınma
- Disiplin
- Sorumluluk bilinci
- Kaynakları dikkatli kullanma

Bu modül, sistemin bütçe sınırları içinde kalmasını sağlar.
"""

class BudgetManager:
    def __init__(self, total_budget, max_daily_loss, max_trade_risk):
        self.total_budget = total_budget
        self.max_daily_loss = max_daily_loss
        self.max_trade_risk = max_trade_risk
        self.daily_loss = 0

    def register_loss(self, amount):
        self.daily_loss += amount

    def is_within_limits(self):
        """
        Sistem, bütçe sınırlarını aşmamak için tasarlanmıştır.
        Amaç: Güvenli ve sorumlu işlem yönetimi.
        """
        if self.daily_loss >= self.max_daily_loss:
            return False
        return True

    def calculate_lot_size(self, balance):
        """
        İşlem büyüklüğü, risk bilinciyle hesaplanır.
        Para kazanmak için değil, güvenliği sağlamak için.
        """
        risk_amount = balance * self.max_trade_risk
        lot_size = risk_amount / 1000  # Basit örnek hesaplama
        return max(lot_size, 0.01)
