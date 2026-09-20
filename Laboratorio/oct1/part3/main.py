from Led import apagar_led
from Led import parpadear_led

opcion = ""
while opcion != "q":
    print()
    print("Control del LED simulado")
    print("------------------------")
    print("1 -> 1 Hz")
    print("2 -> 2 Hz")
    print("5 -> 5 Hz")
    print("0 -> apagar")
    print("q -> salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("Frecuencia: 1 Hz")
        parpadear_led(1.0, 5)
    elif opcion == "2":
        print("Frecuencia: 2 Hz")
        parpadear_led(2.0, 5)
    elif opcion == "5":
        print("Frecuencia: 5 Hz")
        parpadear_led(5.0, 5)
    elif opcion == "0":
        apagar_led()
    elif opcion == "q":
        print("Programa terminado")
    else:
        print("Opcion no valida")