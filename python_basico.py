"""
Módulo de Utilidades Básicas en Python.

Este módulo proporciona funciones y utilidades básicas para ayudar en tareas comunes de Python.
Incluye ejemplos y conceptos fundamentales.
"""

# ! 2. Sintaxis en Python
# * 2.1. Asignación

# Guardar una var un string e imprimir el caracter en la posición 0, longitud y el string completo
ANY_LETTER = "Hola mundo"

print(ANY_LETTER[0])
print(len(ANY_LETTER))
print(ANY_LETTER)

# Guardar un número, imprimirlo, cambiarle el valor e imprimirlo nuevamente
ANY_NUMBER = 10
print(ANY_NUMBER)

ANY_NUMBER = 11
print(ANY_NUMBER)


# Guardar los dos valores booleanos en dos variables diferentes e imprimirlos
ANY_TRUE = True
ANY_FALSE = False
print(ANY_FALSE, ANY_TRUE)

# Asignar 3 números a 3 variables e imprimir
A, B, C = 1, 2, 3
print(A, B, C)

# Guardar un valor None e imprimirlo
ANY_NONE = None
print(ANY_NONE)

# * 2.2. Control de flujo

# Guardar un valor y verificar si es 99, mayor que 200 y ninguno de los dos
Z = 200
if Z == 99:
    print("Es 99")
elif Z > 200:
    print("Es mayor")
else:
    print("Cualquier otra cosa")

# Imprimir valores del 1 al 10 e imprimirlos con for
for i in range(10):
    print(i)

# Imprimir valores del 1 al 10 e imprimirlos con while
VALUE = 1
while VALUE <= 10:
    print(VALUE)
    VALUE += 1

# * 2.3. Estructuras de datos

# Guardar en una tupla 3 valores e imprimir
MyTupla = (1, 2, 3)
print(MyTupla)

# Hacer una lista con tres valores, imprimir el primero
# añadir un cuarto e imprimir la longitudo y los elementos
Mylist = [4, 5, 6]
print(f"Primer Valor: {Mylist[0]}")

Mylist.append(7)
print(f"Longitud: {len(Mylist)}\nToda la lista: {Mylist}")

# Crear un diccionario con 3 valores e imprimir el primero y cambiarle el valor
# Mostrar las claves y valores del diccionario y
# finalmente, imprimir todos los valores con un bucle

MyDict = {"a": 1, "b": 2, "c": 3}
print(f"Primer Valor: {MyDict['a']}")
MyDict["a"] = 11
print(f"Valor a cambiado: {MyDict['a']}")
print(f"Mostrar claves: {MyDict.keys()}")
print(f"Mostrar valores: {MyDict.values()}")
for values in MyDict.values():
    print(values)

def suma(a,b):
    """
    Funcion para sumar dos parametros
    """
    return a + b

RESULT = suma(5,5)

print(RESULT)
