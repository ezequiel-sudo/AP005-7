mylista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
i = -1
while i < 0:
    print("""
    Programa para manipular las listas, selecciona que quieres hacer con la lista: 
    1.Agregar un elemento o varios
    2.Eliminar un elemento
    3.Tamaño de la lista
    4.Eliminar todos los elementos de la lista
    5.Invertir""")
    opcion = input('Ingrese que quiere hacer con la lista: ')
    print(mylista)
    match opcion:
        case '1':
            num = int(input('Ingrese el numero de elementos que quiere ingresar a la lista: '))
            for x in range(0, num):
                var = input('Ingrese el elemento que quiere agregar a la lista: ')
                mylista.append(var)
        case '2':
            var = input('Ingrese el elemento que quiere eliminar de la lista: ')
            mylista.remove(var)
        case '3':
            print('La lista tiene un tamaño de :', len(mylista))
        case '4':
            mylista.clear()
        case '5':
            mylista.reverse()
    print(mylista)