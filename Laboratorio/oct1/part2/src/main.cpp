#include <Arduino.h>
#include "Led.h"

float frecuenciaHz = 1.0;

void setup()
{
    Serial.begin(115200);
    iniciarLed(4);
    Serial.println();
    Serial.println("Control del LED integrado");
    Serial.println("-------------------------");
    Serial.println("1 -> 1 Hz");
    Serial.println("2 -> 2 Hz");
    Serial.println("5 -> 5 Hz");
    Serial.println("0 -> apagar");
    Serial.println();
}

void loop()
{
    if (Serial.available() > 0)
    {
        char opcion = Serial.read();
        if (opcion == '1')
        {
            frecuenciaHz = 1.0;
            Serial.println("Frecuencia: 1 Hz");
        }
        else if (opcion == '2')
        {
            frecuenciaHz = 2.0;
            Serial.println("Frecuencia: 2 Hz");
        }
        else if (opcion == '5')
        {
            frecuenciaHz = 5.0;
            Serial.println("Frecuencia: 5 Hz");
        }
        else if (opcion == '0')
        {
            frecuenciaHz = 0.0;
            apagarLed();
            Serial.println("LED apagado");
        }
    }
    if (frecuenciaHz > 0.0)
    {
        parpadearLed(frecuenciaHz);
    }
}