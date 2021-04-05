import numpy as np

# Método para llenar la matriz
def fillMatrix(row, column):
    matrix = []
    aux = []

    # Se hace una listas de listas, en las que cada lista equivale a una fila de la matriz
    for n in range(row):
        for m in range(column):
            aux.append(int(input(f'Digite el número de la posición {n}, {m} de la matriz: ')))
        matrix.append(aux)
        aux.clear()

    return np.asmatrix(matrix)

rows1=input('Defina las filas de la matriz 1: ')
columns1=input('Defina las columnas de la matriz 1: ')

rows2=input('Defina las filas de la matriz 2: ')
columns2=input('Defina las columnas de la matriz 2: ')

array1 = fillMatrix(rows1, columns1)
array2 = fillMatrix(rows2, columns2)

