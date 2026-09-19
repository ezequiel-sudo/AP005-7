import network
import time
import urequests
import ujson
from machine import ADC, Pin

SSID = ''
PASSWORD = ''
AIO_USER = ''
AIO_KEY = ''
FEED_NAME = 'potenciometro'

adc = ADC(Pin(4))
adc.atten(ADC.ATTN_11DB) # Atenuación para leer el rango completo 0-3.3V

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a la red Wi-Fi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            print(".", end="")
    print('\nConexión exitosa. IP:', wlan.ifconfig()[0])

def enviar_dato(voltaje):
    url = f"https://io.adafruit.com/api/v2/{AIO_USER}/feeds/{FEED_NAME}/data"
    headers = {'X-AIO-Key': AIO_KEY, 'Content-Type': 'application/json'}
    data = {'value': voltaje}
    
    try:
        response = urequests.post(url, data=ujson.dumps(data), headers=headers)
        print("Servidor respondió:", response.status_code)
        response.close()
    except Exception as e:
        print("Error enviando dato:", e)

conectar_wifi()

while True:

    lectura = adc.read()
    voltaje = (lectura / 4095.0) * 3.3
    
    print(f"Lectura ADC: {lectura} | Voltaje: {voltaje:.2f} V")
    enviar_dato(voltaje)
    
    # Pausa de 5 segundos Adafruit IO gratuito permite 30 envíos por minuto
    time.sleep(5)
