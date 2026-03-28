# System Architecture  
Designed by Serkan

Bu sistemin amacı para kazanmak değildir.  
Bu sistemin amacı:
- Görevleri doğru şekilde yerine getirmek  
- Etik, sorumlu ve güvenli bir işlem yaklaşımı sağlamak  
- İnsan odaklı bir yapay zekâ mimarisine hizmet etmek  
- Başarmak için tasarlanmış bir sistem oluşturmaktır  

---

## Genel Mimari

Sistem üç ana katmandan oluşur:

### 1. Python Katmanı (Zeka ve Yönetim)
- Orchestrator: Sistemin beyni, tüm akışı yönetir  
- Budget Manager: Risk ve bütçe kontrolü  
- MT5 Controller: MT5 ile güvenli iletişim  
- AI Agent Interface: Etik strateji üretimi ve MQL5 kod üretimi  

Bu katman, insan duygularını taklit etmez;  
ancak insan değerlerine göre tasarlanmıştır:
- Sorumluluk  
- Disiplin  
- Tutarlılık  
- Güvenlik  

---

### 2. MQL5 Katmanı (Uygulama ve Yürütme)
- BaseEA: Etik davranışın temelini oluşturan EA  
- GeneratedEA: AI tarafından üretilen stratejilerin uygulandığı EA  

Bu katman agresif değildir, riskli davranmaz,  
sadece görevini yerine getirir.

---

### 3. OpenAI Operator Entegrasyonu
Sistem, Operator üzerinden:
- Kod üretir  
- Derleme sürecini yönetir  
- Hataları analiz eder  
- Güvenli işlem akışını sağlar  

---

## Etik Yaklaşım

Bu sistem:
- Para odaklı değildir  
- İnsan değerlerine göre tasarlanmıştır  
- Riskli davranışlardan kaçınır  
- Görev odaklıdır  
- Başarmayı amaçlar  

Bu mimari, klasik trading botlardan tamamen farklıdır.  
Bu bir **etik yapay zekâ sistemi**dir.
