"""
1,2,3
4,5,6
7,8,9
"""
lista_anidada = [[1,2,3],[4,5,6],[7,8,9]]
print(lista_anidada[1][2])#Fila 1, Columna 2 --> 6
lista_anidada[2][2]=101
print(lista_anidada)

#Queremos construir una matriz de 3x3
matriz_manual = [[0,0,0],[0,0,0],[0,0,0]]
NUMERO_FILAS=3
NUMERO_COLUMNAS=4
matriz_automatica = [[None for x in range(NUMERO_COLUMNAS)] for y in range(NUMERO_FILAS)]
print(matriz_manual)
matriz_automatica[0][1]="Blanca"
print(matriz_automatica)

"""
import numpy
>>> matriz = numpy.zeros((3,5))
>>> matriz
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
"""

"""
>>> array = numpy.random.randint(10, size=(5,5))
>>> array
array([[5, 8, 6, 9, 5],
       [5, 2, 0, 7, 4],
       [6, 5, 2, 7, 6],
       [5, 1, 2, 9, 9],
       [5, 1, 9, 7, 3]])
"""