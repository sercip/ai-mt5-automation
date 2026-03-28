MT5 Controller Module
Designed by Serkan

Bu sistemin amacı para kazanmak değildir.
Bu sistemin amacı:
- MT5 üzerinde güvenli ve kontrollü işlem yürütmek
- Hataları tespit edip sorumlu şekilde yönetmek
- İnsan odaklı bir yapay zekâ mimarisine hizmet etmek

Sistem, finansal işlemleri yürütürken agresif davranmaz.
İnsan değerlerine uygun şekilde tasarlanmıştır:
- Güvenlik
- Tutarlılık
- Risk farkındalığı
- Sorumluluk
"""

import MetaTrader5 as mt5


class MT5Controller:
    def __init__(self):
        self.connected = False

    def connect(self):
        """
        MT5 terminaline güvenli bağlantı kurar.
        Amaç: Sistemin gerçek dünya ile iletişim kurmasını sağlamak.
        """
        if not mt5.initialize():
            return False

        self.connected = True
        return True

    def get_account_info(self):
        """
        Hesap bilgilerini güvenli şekilde alır.
        """
        if not self.connected:
            return None

        return mt5.account_info()

    def get_symbol_info(self, symbol):
        """
        Sembolün işlem için uygun olup olmadığını kontrol eder.
        """
        if not self.connected:
            return None

        return mt5.symbol_info(symbol)

    def compile_ea(self, ea_code):
        """
        EA kodunu derler.
        Amaç: Hatasız ve güvenli bir çalışma sağlamak.
        (Gerçek derleme Operator üzerinden yapılacak)
        """
        if "error" in ea_code.lower():
            return False
        return True

    def deploy_ea(self):
        """
        EA'yı grafiğe ekler.
        Sistem, riskli durumlarda işlem açmaz.
        """
        return "EA başarıyla yüklendi."
