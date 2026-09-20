from machine import Pin
import time

pin_led = None

def iniciar_led(numero_pin):
    global pin_led
    pin_led = Pin(numero_pin, Pin.OUT)
    apagar_led()

def encender_led():
    pin_led.value(1)

def apagar_led():
    pin_led.value(0)

def parpadear_led(frecuencia_hz):
    if frecuencia_hz <= 0:
        apagar_led()
        return
    medio_periodo_ms = int(500 / frecuencia_hz)
    encender_led()
    time.sleep_ms(medio_periodo_ms)
    apagar_led()
    time.sleep_ms(medio_periodo_ms)