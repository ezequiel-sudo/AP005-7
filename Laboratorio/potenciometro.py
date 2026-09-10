from machine import Pin, ADC
import time

potenciometro = ADC(Pin(4)) 
led = Pin(2, Pin.OUT)       

# ATTN_11DB permite que el ADC lea voltajes hasta 3.3V.
potenciometro.atten(ADC.ATTN_11DB) 

umbral_voltaje = 2.0

while True:
    lectura = potenciometro.read_u16()
    voltaje_actual = lectura * (3.3 / 65535)
    
    if voltaje_actual > umbral_voltaje:
        led.value(1)
    else:
        led.value(0)
        
    time.sleep(0.1)
