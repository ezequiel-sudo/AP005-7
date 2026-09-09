# Los diccionarios se usan para almacenar valores en pares clave:valor.
# Son ordenados (desde Python 3.7), modificables y no permiten claves duplicadas.

# 1. Crear un diccionario
menu = {"avena": 3, "tostada": 6, "jugo": 5, "muffin": 2}
print("Diccionario original:", menu)

# 2. Acceder a los valores
print("Precio del jugo:", menu["jugo"])
print("Precio de la tostada usando get():", menu.get("tostada"))

# 3. Comprobar si una clave existe (Evitar errores)
if "hamburguesa" in menu:
    print(menu["hamburguesa"])
else:
    print("La hamburguesa no está en el menú.")

# 4. Agregar y actualizar valores
menu["pastel"] = 8 # Agrega una nueva clave-valor
print("Después de agregar pastel:", menu)

menu["avena"] = 5 # Modifica el valor de una clave existente
print("Después de modificar avena:", menu)

# Actualizar múltiples valores a la vez
menu.update({"te": 2, "cafe": 3})
print("Después de update:", menu)

# 5. Eliminar elementos
elemento_eliminado = menu.pop("muffin") # Elimina y devuelve el valor
print("Se eliminó el muffin que costaba:", elemento_eliminado)
print("Diccionario después de pop:", menu)

# 6. Obtener todas las claves, valores y pares (items)
print("\n--- Iterando el diccionario ---")
# Obtener claves
print("Claves del menú:", list(menu.keys()))

# Iterar sobre las claves
for clave in menu.keys():
    print("Clave:", clave)

# Iterar sobre los valores
for valor in menu.values():
    print("Valor:", valor)

# Iterar sobre pares clave:valor
for clave, valor in menu.items():
    print(f"El producto {clave} cuesta {valor} dólares.")

# 7. Crear un diccionario a partir de dos listas (Dict Comprehension con zip)
nombres = ['Ana', 'Juan', 'Pedro']
edades = [25, 30, 22]

diccionario_edades = {clave: valor for clave, valor in zip(nombres, edades)}
print("\nDiccionario creado con zip():", diccionario_edades)