"""Este script demuestra el uso básico de la biblioteca NumPy para trabajar con arrays en Python."""

#! Arrays

# Crear un array e imprimir sus valores y tamaño
import numpy as np

Mylist = [1, 2, 3]

myArray = np.array(Mylist)

print(myArray)
print(myArray.shape)

# Hacer una mariz 2x3 e imprimir la primera y última lista
# Luego imprimir un elemento concreto y los valores de la columna 3

myMatriz = [[1, 2, 3], [4, 5, 6]]
myArray = np.array(myMatriz)
print(myArray)
print(myArray.shape)
print(myArray[0])
print(myArray[-1])
print(myArray[0, 2])
print(myArray[:, 2])

#! Operaciones

myArray1 = np.array([2, 2, 2])
myArray2 = np.array([3, 3, 3])

print(myArray1 + myArray2)
print(myArray1 * myArray2)
