"""
Logging Engine
Designed by Serkan

Bu modül, sistemin tüm önemli olaylarını kaydeder.
Amaç:
- Şeffaflık
- İzlenebilirlik
- Hata tespiti
- Güvenli işlem geçmişi

Loglar hem konsola hem de dosyaya yazılabilir.
"""

import datetime
import os

class LoggingEngine:
    def __init__(self, log_directory="logs"):
        self.log_directory = log_directory

        # Klasör yoksa oluştur
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Günlük log dosyası
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        self.log_file = os.path.join(log_directory, f"log_{date_str}.txt")

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message, level="INFO"):
        """
        Mesajı hem konsola hem dosyaya yazar.
        """
        timestamped = f"[{self._timestamp()}] [{level}] {message}"

        # Konsola yaz
        print(timestamped)

        # Dosyaya yaz
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(timestamped + "\n")

    def info(self, message):
        self.log(message, level="INFO")

    def warning(self, message):
        self.log(message, level="WARNING")

    def error(self, message):
        self.log(message, level="ERROR")
