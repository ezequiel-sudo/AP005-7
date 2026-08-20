from machine import Pin
import neopixel
import time

pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(pin, 1)
cont = 0
for cont in range(10):
    print('blink ', cont+1)
    # Set to RED (RGB format: Red=255, Green=0, Blue=0)
    np[0] = (64, 128, 255)
    np.write()
    time.sleep(1)
    
    # Turn OFF (RGB format: 0, 0, 0)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
