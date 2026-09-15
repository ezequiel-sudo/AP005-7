# Las tuplas son similares a las listas, pero son INMUTABLES (no se pueden cambiar, agregar o eliminar elementos una vez creadas).
# Son ordenadas y permiten valores duplicados.

# 1. Crear una tupla
mi_tupla = ('Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde')
print("Tupla original:", mi_tupla)

# 2. Acceder a elementos
print("Primer elemento:", mi_tupla[0])
print("Tercer elemento:", mi_tupla[2])

# 3. Evaluar si un elemento está en la tupla
print("¿Está 'Rojo' en la tupla?:", 'Rojo' in mi_tupla)

# 4. Contar elementos
print("Cantidad de veces que aparece 'Azul':", mi_tupla.count('Azul'))

# 5. Tupla con un solo elemento (debe tener una coma al final)
tupla_unitaria = ('Blanco',)
print("Tupla de un solo elemento:", tupla_unitaria)
print("Tipo de dato:", type(tupla_unitaria))

# 6. Empaquetado de tupla (crear tupla sin paréntesis)
tupla_datos = 'Gaspar', 5, 8, 1999
print("Tupla empaquetada:", tupla_datos)

# 7. Desempaquetado de tupla (asignar valores a variables)
nombre, dia, mes, anno = tupla_datos
print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {anno}")

# 8. Convertir una tupla a lista (para poder modificarla)
lista_desde_tupla = list(mi_tupla)
lista_desde_tupla.append('Negro') # Ahora que es lista, sí podemos agregar
print("Tupla convertida a lista y modificada:", lista_desde_tupla)

# Convertir de nuevo a tupla
mi_tupla_modificada = tuple(lista_desde_tupla)
print("Lista convertida nuevamente a tupla:", mi_tupla_modificada)