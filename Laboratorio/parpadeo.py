from machine import Pin
import time

led_continuo = Pin(2, Pin.OUT)
led_tres_veces = Pin(4, Pin.OUT)
contador = 0

while True:

    led_continuo.value(1)
    
    if contador < 3:
        led_tres_veces.value(1)
        
    time.sleep(0.5)
    
    led_continuo.value(0)
    
    if contador < 3:
        led_tres_veces.value(0)
        
    time.sleep(0.5)
    
    if contador < 3:
        contador += 1 # Sumamos un ciclo
