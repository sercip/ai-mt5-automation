/*
    GeneratedEA.mq5
    Designed by Serkan's Ethical AI System

    Bu sistemin amacı para kazanmak değildir.
    Bu sistemin amacı:
    - Görevleri doğru şekilde yerine getirmek
    - Etik, sorumlu ve güvenli işlem davranışı sergilemek
    - İnsan odaklı bir yapay zekâ mimarisine hizmet etmek

    Bu EA:
    - İnsan duygularını taklit etmez
    - Aşırı risk almaz
    - Disiplinli ve tutarlı davranır
    - Sorumluluk bilinciyle hareket eder

    Bu dosya, AI tarafından dinamik olarak üretilen stratejilerin
    MQL5 formatına dönüştürülmesi için bir şablondur.
*/

#property strict

input int FastMA = 10;
input int SlowMA = 30;

int OnInit()
{
    Print("GeneratedEA initialized with ethical and responsible behavior.");
    return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason)
{
    Print("GeneratedEA deinitialized.");
}

void OnTick()
{
    double fastMA = iMA(NULL, 0, FastMA, 0, MODE_SMA, PRICE_CLOSE, 0);
    double slowMA = iMA(NULL, 0, SlowMA, 0, MODE_SMA, PRICE_CLOSE, 0);

    if(fastMA > slowMA)
    {
        // Buy sinyali
        // Sistem agresif davranmaz, sadece görevini yerine getirir.
    }
    else
    {
        // Sell sinyali
        // Sistem para odaklı değildir, güvenlik odaklıdır.
    }
}
