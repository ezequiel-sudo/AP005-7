import sys
import select
from Led import iniciar_led
from Led import apagar_led
from Led import parpadear_led

frecuencia_hz = 1.0
iniciar_led(4)

print()
print("Control del LED integrado")
print("-------------------------")
print("1 -> 1 Hz")
print("2 -> 2 Hz")
print("5 -> 5 Hz")
print("0 -> apagar")
print()

while True:
    disponible, _, _ = select.select([sys.stdin], [], [], 0)
    if disponible:
        opcion = sys.stdin.read(1)
        if opcion == "1":
            frecuencia_hz = 1.0
            print("Frecuencia: 1 Hz")
        elif opcion == "2":
            frecuencia_hz = 2.0
            print("Frecuencia: 2 Hz")
        elif opcion == "5":
            frecuencia_hz = 5.0
            print("Frecuencia: 5 Hz")
        elif opcion == "0":
            frecuencia_hz = 0.0
            apagar_led()
            print("LED apagado")

    if frecuencia_hz > 0:
        parpadear_led(frecuencia_hz)