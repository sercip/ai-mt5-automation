```markdown
# Serkan's Ethical AI Trading System  
Modüler, güvenli, izlenebilir ve sürekli geliştirilebilir bir otomatik işlem mimarisi.

Bu proje, yapay zekâya verilen sermayeyi **nasıl yönettiğini gözlemlemek**,  
**davranışını analiz etmek**, **sürekli geliştirmek** ve  
uzun vadede profesyonel bir finans operatörü gibi çalışmasını sağlamak amacıyla tasarlanmıştır.

Sistem; AI, güvenlik, loglama, MT5 bağlantısı ve operatör kontrolü gibi  
katmanlardan oluşan profesyonel bir mimariye sahiptir.

---

## 🚀 Amaç

Bu sistemin amacı:

- AI’nın sermaye yönetim davranışını gözlemlemek  
- Bu davranışı zaman içinde geliştirmek  
- Riskleri kontrol altında tutmak  
- Modüler ve genişletilebilir bir mimari sunmak  
- MT5 üzerinde disiplinli, tutarlı ve şeffaf işlem yürütmek  
- Uzun vadede AI’nın profesyonel bir finans operatörü gibi çalışmasını sağlamak  

Bu proje **kâr odaklı değildir**.  
Odak noktası **davranış analizi + gelişim + profesyonel mimari**dir.

---

## 🧩 Mimari Yapı

Proje aşağıdaki modüllerden oluşur:

```
python/
│
├── ai_agent_interface.py   → Yapay zekâ strateji üreticisi
├── mt5_controller.py       → MT5 bağlantı ve işlem kontrol katmanı
├── safety_engine.py        → Risk ve güvenlik filtresi
├── logging_engine.py       → Loglama ve izlenebilirlik sistemi
├── orchestrator.py         → Sistemin beyni (tüm modülleri yönetir)
└── operator_client.py      → Operatör arayüzü (manuel kontrol)
```

Her dosya **tek sorumluluk prensibi** ile yazılmıştır.  
Modüller birbirine sıkı bağlı değildir; bu sayede sistem genişletilebilir.

---

## 🧠 Modüllerin Açıklaması

### **1. AI Agent Interface**
- Strateji üretir  
- MQL5 kodu oluşturabilir  
- Gerçek AI modeline bağlanmaya hazırdır  
- Şu anda simülasyon modundadır  

### **2. MT5 Controller**
- MT5 terminaline bağlanır  
- İşlem açar / kapatır  
- Bağlantı durumunu yönetir  
- Orchestrator dışında kimse doğrudan kullanmaz  

### **3. Safety Engine**
- Risk limitlerini uygular  
- Yasaklı sembolleri engeller  
- Lot miktarını güvenli seviyeye çevirir  
- Confidence değerlerini kontrol eder  

### **4. Logging Engine**
- Tüm olayları kayıt altına alır  
- Strateji logları  
- İşlem logları  
- Sistem logları  
- İzlenebilirlik sağlar  

### **5. Orchestrator**
- Sistemin beynidir  
- AI → Safety → MT5 akışını yönetir  
- Operatör isteklerini işler  
- Her modülü koordine eder  

### **6. Operator Client**
- Manuel işlem açma isteği  
- Manuel kapatma isteği  
- AI strateji önizleme  
- Log okuma  
- Sistem durumu görüntüleme  

---

## 🔒 Sistem Felsefesi

**“Bu sistem, AI’nın sermaye yönetim davranışını sürekli geliştirerek, sonunda profesyonel bir finans operatörü gibi çalışmasını sağlamak için tasarlanmıştır.”**

- Sistem kontrollü çalışır  
- Risk yönetimi otomatik uygulanır  
- Tüm kararlar izlenebilir  
- Loglama zorunludur  
- AI’nın davranışı şeffaf şekilde gözlemlenir  

Bu proje herhangi bir “insan vs AI” felsefesine dayanmaz.  
Odak tamamen **performans**, **davranış**, **gelişim** ve **mühendisliktir**.

---

## ▶️ Çalıştırma

1. Python ortamını hazırlayın  
2. MT5 terminalinin açık olduğundan emin olun  
3. Orchestrator’ı başlatın:

```bash
python orchestrator.py
```

4. Operatör arayüzü ile etkileşime geçin:

```python
from operator_client import OperatorClient
```

---

## 📌 Notlar

- Sistem modülerdir, her katman bağımsız geliştirilebilir  
- AI gerçek modele bağlanmaya hazırdır  
- Safety Engine genişletilebilir  
- Logging Engine profesyonel format kullanır  
- Orchestrator tüm akışı yönetir  

---

## 👤 Tasarımcı

Bu mimari **Serkan** tarafından tasarlanmış,  
AI davranış analizi ve profesyonel finans otomasyonu vizyonu ile geliştirilmiştir.

```
“Davranış + Gelişim + Profesyonel Mimari”
```

---

## 📄 Lisans

Bu proje kişisel kullanım içindir.  
Ticari kullanım için izin gereklidir.
```

