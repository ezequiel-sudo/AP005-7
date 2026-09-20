import time

def encender_led():
    print("[***] LED ENCENDIDO")

def apagar_led():
    print("[   ] LED APAGADO")

def parpadear_led(frecuencia_hz, ciclos):
    if frecuencia_hz <= 0:
        apagar_led()
        return
    medio_periodo_s = 0.5 / frecuencia_hz
    for i in range(ciclos):
        encender_led()
        time.sleep(medio_periodo_s)
        apagar_led()
        time.sleep(medio_periodo_s)