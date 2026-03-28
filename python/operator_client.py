"""
Operator Client
Designed by Serkan

Bu modül, sistemin dış dünya ile iletişim kurmasını sağlar.
Gerçek bir operatör sistemi ile entegre edilebilir.
Şimdilik simülasyon modunda çalışır.
"""

class OperatorClient:
    def __init__(self):
        self.connected = False

    def connect(self):
        """
        Operatör sistemine bağlantı kurar.
        Şimdilik her zaman başarılı döner.
        """
        self.connected = True
        return True

    def send_task(self, task_type, payload):
        """
        Operatöre görev gönderir.
        Gerçek sistemde API çağrısı yapılır.
        Şimdilik simülasyon cevabı döner.
        """
        if not self.connected:
            return {"status": "error", "message": "Operator bağlantısı yok"}

        return {
            "status": "success",
            "task_type": task_type,
            "payload": payload,
            "response": "Simulated operator response"
        }

    def is_safe(self, content):
        """
        İçeriğin güvenli olup olmadığını kontrol eder.
        Basit bir filtreleme mekanizması.
        """
        forbidden = ["risk", "danger", "hack", "exploit"]
        content_lower = content.lower()

        for word in forbidden:
            if word in content_lower:
                return False

        return True
