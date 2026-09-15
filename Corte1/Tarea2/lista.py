# Las listas se utilizan para almacenar varios elementos en una sola variable.
# Son ordenadas, mutables (modificables) y permiten valores duplicados.

# 1. Crear una lista
mi_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
print("Lista original:", mi_lista)

# 2. Acceder a elementos y conocer el tamaño
print("Elemento en la posición 2:", mi_lista[2]) # Imprime 'Amarillo'
print("Tamaño de la lista:", len(mi_lista))

# 3. Slicing (Cortar listas)
print("Elementos del 0 al 2:", mi_lista[0:2])
print("Elementos hasta el índice 2:", mi_lista[:2])

# 4. Agregar elementos
mi_lista.append('Blanco') # Agrega al final
print("Lista después de append('Blanco'):", mi_lista)

mi_lista.insert(3, 'Negro') # Inserta en una posición específica
print("Lista después de insert(3, 'Negro'):", mi_lista)

mi_lista.extend(['Marron', 'Gris']) # Concatena otra lista
print("Lista después de extend:", mi_lista)

# 5. Encontrar el índice de un elemento
print("El color 'Azul' está en el índice:", mi_lista.index('Azul'))

# 6. Eliminar elementos
mi_lista.remove('Marron') # Elimina por valor
print("Lista después de remove('Marron'):", mi_lista)

elemento_eliminado = mi_lista.pop() # Elimina el último elemento
print("Elemento eliminado con pop():", elemento_eliminado)
print("Lista después de pop:", mi_lista)

# 7. Ordenar una lista
mi_lista_numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Lista de números desordenada:", mi_lista_numeros)

mi_lista_numeros.sort() # Ordena de menor a mayor
print("Lista ordenada de menor a mayor:", mi_lista_numeros)

mi_lista_numeros.sort(reverse=True) # Ordena de mayor a menor
print("Lista ordenada de mayor a menor:", mi_lista_numeros)