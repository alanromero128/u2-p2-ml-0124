import numpy as np
# Alan Romero NC 0124
# Ejemplos de numpy Numerical Python
print("-- Espaciado Linealmente en array -- 0124")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- Matriz identidad en 2D array -- 0124")
matrix=np.eye(3)
print(matrix)
print("-- Genera numeros al azar(aleatorio) en 2D array -- 0124")
numale=np.random.random((3,4)) #genera 12 numeros aleatorios 
print(numale)
print("generar 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) #genera 12 numeros aleatorios 
print(numale)
# como generar numeros 9 aleatorios comprendidos entre  1 y 20 
# con numpy en un arreglo de 3 por 3 
print("Generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)
print("Alan Romero NC 0124")