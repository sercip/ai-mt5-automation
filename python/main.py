"""
Main Automation Loop
Designed by Serkan

Bu sistemin amacı:
- Otomatik, etik ve sorumlu bir işlem akışı sağlamak
- İnsan müdahalesine ihtiyaç duymadan görevini doğru şekilde yerine getirmek
- Para kazanmak için değil, başarmak için çalışmak

Bu dosya, sistemin otomatik döngüsünü başlatır.
"""

import time
from orchestrator import Orchestrator
from budget_manager import BudgetManager
from mt5_controller import MT5Controller
from ai_agent_interface import AIAgentInterface


def main():
    # Başlangıç parametreleri (örnek değerler)
    total_budget = 10000
    max_daily_loss = 200
    max_trade_risk = 0.01  # %1

    budget_manager = BudgetManager(
        total_budget=total_budget,
        max_daily_loss=max_daily_loss,
        max_trade_risk=max_trade_risk
    )

    mt5 = MT5Controller()
    ai_agent = AIAgentInterface()

    orchestrator = Orchestrator(
        budget_manager=budget_manager,
        mt5_controller=mt5,
        ai_agent=ai_agent
    )

    print("Etik otomasyon sistemi başlatılıyor...")

    while True:
        result = orchestrator.run_cycle()
        print(f"[DÖNGÜ SONUCU] {result}")

        # Burada örnek olarak her döngüde küçük bir kayıp kaydediyoruz (simülasyon)
        budget_manager.register_loss(10)

        # Döngüler arasında bekleme süresi (örnek: 60 saniye)
        time.sleep(60)


if __name__ == "__main__":
    main()
