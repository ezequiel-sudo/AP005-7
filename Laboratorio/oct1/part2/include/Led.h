#ifndef LED_H
#define LED_H
#include <Arduino.h>
void iniciarLed(uint8_t pin);
void encenderLed();
void apagarLed();
void parpadearLed(float frecuenciaHz);
#endif