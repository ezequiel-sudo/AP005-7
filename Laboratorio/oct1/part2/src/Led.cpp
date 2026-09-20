#include "Led.h"
uint8_t pinLed;

void iniciarLed(uint8_t pin)
{
    pinLed = pin;
    pinMode(pinLed, OUTPUT);
    apagarLed();
}

void encenderLed()
{
    digitalWrite(pinLed, HIGH);
}

void apagarLed()
{
    digitalWrite(pinLed, LOW);
}

void parpadearLed(float frecuenciaHz)
{
    if (frecuenciaHz <= 0.0)
    {
        apagarLed();
        return;
    }
    unsigned long medioPeriodoMs = 500.0 / frecuenciaHz;
    encenderLed();
    delay(medioPeriodoMs);
    apagarLed();
    delay(medioPeriodoMs);
}