# AI‑Driven MetaTrader 5 Autonomous Trading System  
### Designed, Architected and Directed by Serkan

## 📌 Overview
Bu proje, MetaTrader 5 üzerinde tam otonom çalışan bir işlem otomasyon sistemi geliştirme vizyonunun ürünüdür.  
Sistem; MQL5 Expert Advisor üretimi, Python tabanlı orkestrasyon, hata tespiti, otomatik düzeltme, strateji adaptasyonu ve bütçe yönetimi gibi bileşenleri tek bir çatı altında toplar.

Amaç, klasik “EA yaz – compile et – grafiğe ekle” döngüsünü tamamen ortadan kaldırıp, **kendi kendini yöneten bir trading zekâsı** oluşturmaktır.

Bu proje, insan gözetimi olmadan:
- Strateji üretebilen  
- EA yazabilen  
- Derleyebilen  
- MT5 üzerinde çalıştırabilen  
- Hataları analiz edip düzeltebilen  
- Risk ve bütçe yönetimi yapabilen  
- Kendi kendine optimize olabilen  

bir **agentic trading system** mimarisidir.

---

## 🎯 Amaç
Bu proje, sadece bir EA üretmek için değil;  
**MT5 üzerinde tam otonom bir yapay zekâ ajanının çalışabilmesi için gerekli altyapıyı kurmak** amacıyla tasarlandı.

Sistem şu yetenekleri hedefler:
- MQL5 EA dosyalarını otomatik üretme  
- MetaEditor üzerinden compile etme  
- EA’yı grafiğe ekleme  
- AutoTrading kontrolü  
- Log takibi ve hata tespiti  
- Hatalara göre EA kodunu yeniden üretme  
- Strateji optimizasyon döngüleri  
- **Python tarafına verilen bir bütçeyi yönetme ve bu bütçeyi kendi kararlarıyla kullanma**  
  - İşlem başına risk ayarlama  
  - Pozisyon büyüklüğü hesaplama  
  - Günlük/haftalık kayıp limitleri  
  - Bütçe tükenince sistemi durdurma veya strateji değiştirme  

Bu yapı, gerçek anlamda **otonom finansal karar verme** sisteminin temelini oluşturur.

---

## 🧠 Neden OpenAI Operator?
Standart LLM’ler:
- MT5’i açamaz  
- MetaEditor’da compile edemez  
- EA’yı grafiğe sürükleyemez  
- AutoTrading’i aktif edemez  
- Log okuyup aksiyon alamaz  
- Ekran üzerinden karar veremez  

Bu proje, tam da bu nedenle **OpenAI Operator** için gerçek bir kullanım senaryosudur.

Operator’ın sağlayacağı:
- Ekran anlama  
- Mouse/klavye kontrolü  
- Uygulama seviyesinde otomasyon  
- Hata sonrası kendi kendine düzeltme  
- Çok adımlı görev planlama  

gibi yetenekler, bu sistemi tam otonom hale getirecek.

---

## 🧩 Sistem Mimarisi


Serkan (Mimar)
↓
AI Agent (Kod üretimi + hata düzeltme + strateji planlama)
↓
Python Orchestrator (Dosya yönetimi + MT5 entegrasyonu + bütçe yönetimi)
↓
MetaTrader 5 / MetaEditor


### Bileşenler:
- **AI Agent**  
  - Strateji açıklamasından EA üretir  
  - Compile hatalarını analiz eder  
  - Kodu yeniden düzenler  
  - Piyasa koşullarına göre strateji önerir  

- **Python Orchestrator**  
  - EA dosyalarını oluşturur  
  - MetaEditor derleme sürecini tetikler  
  - Logları izler  
  - Bütçe yönetimi yapar  
  - Risk parametrelerini dinamik olarak ayarlar  
  - Gerekirse AI’a geri bildirim gönderir  

- **MT5 / MetaEditor**  
  - EA’yı çalıştırır  
  - İşlemleri yürütür  
  - Log üretir  

---

## 🚀 Özellikler
- Dinamik MQL5 EA üretimi  
- Otomatik derleme  
- Otomatik grafik ekleme  
- AutoTrading kontrolü  
- Log tabanlı adaptasyon  
- Strateji güncelleme döngüleri  
- Çoklu sembol desteği (planlanan)  
- **Bütçe tabanlı risk yönetimi**  
- **Otonom pozisyon büyüklüğü hesaplama**  
- **Kayıp limiti kontrolü**  

---

## 🔮 Yol Haritası
- Risk yönetimi modülü (gelişmiş)  
- Çoklu sembol otonom işlem  
- Portföy seviyesinde karar verme  
- Anomali tespiti  
- Reinforcement Learning tabanlı optimizasyon  
- Tam otonom “meta-brain” kontrol katmanı  
- Bütçe yönetimi için davranışsal ekonomi modelleri  

---

## 🧾 Not
Bu proje, Serkan tarafından tasarlanmış ve geliştirilmekte olan bir **gerçek dünya otonom işlem sistemi** mimarisidir.  
OpenAI Operator erişimi, bu sistemin tam potansiyeline ulaşması için kritik öneme sahiptir.
