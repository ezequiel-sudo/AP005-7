precio = int(input('Ingrese un numero '))

if precio <= 1000:
    print('Barato')
elif precio > 1000 and precio <= 2000:
    print('Medianamente barato')
elif precio > 2000 and precio <= 3000:
    print('Medianamente caro')
else:
    print('Caro')