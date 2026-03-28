"""
Logging Engine
Designed by Serkan

Bu modül, sistemde gerçekleşen her adımı kayıt altına alır.
Amaç:
- Şeffaflık
- Denetlenebilirlik
- Hata ayıklama kolaylığı
- Sistem davranışının izlenebilir olması

Logging Engine:
- İşlem açmaz
- Strateji üretmez
- Karar vermez
- Sadece kayıt tutar
"""

import logging
from datetime import datetime
import os

class LoggingEngine:
    def __init__(self, log_dir="logs", log_file="system.log"):
        """
        :param log_dir: Log dosyalarının tutulacağı klasör
        :param log_file: Ana log dosyası adı
        """

        self.log_dir = log_dir
        self.log_file = log_file

        # Klasör yoksa oluştur
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Log dosyasının tam yolu
        self.full_path = os.path.join(self.log_dir, self.log_file)

        # Logger yapılandırması
        self.logger = logging.getLogger("TradingSystemLogger")
        self.logger.setLevel(logging.INFO)

        # Aynı handler iki kez eklenmesin
        if not self.logger.handlers:
            handler = logging.FileHandler(self.full_path, encoding="utf-8")
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.info("[LoggingEngine] Log sistemi başlatıldı.")

    # -------------------------------------------------------------------------
    # Log fonksiyonları
    # -------------------------------------------------------------------------
    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def critical(self, msg: str):
        self.logger.critical(msg)

    # -------------------------------------------------------------------------
    # Özel kayıt fonksiyonu
    # -------------------------------------------------------------------------
    def log_trade(self, symbol, action, volume, ticket):
        """
        İşlem açıldığında özel bir kayıt oluşturur.
        """
        self.info(
            f"[TRADE] Symbol={symbol} | Action={action} | Volume={volume} | Ticket={ticket}"
        )

    def log_strategy(self, strategy: dict):
        """
        AI stratejisini özel formatta kaydeder.
        """
        self.info(f"[STRATEGY] {strategy}")
