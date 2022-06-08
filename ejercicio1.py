'''
Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementos aleatorios de números enteros del 
0 al 100.
'''
import numpy as np
import random

print("bienvenidos a matrices XD")
#matriz = np.zeros((3,3),dtype=int)
#matriz = np.diag([1,1,1])
matriz = np.ones((3,3),dtype=int)
print(matriz)

for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(0,100)
        
print(matriz)