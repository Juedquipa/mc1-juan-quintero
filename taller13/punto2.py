import numpy as np

# Método para llenar la matriz
def fillMatrix(row, column):
    matrix = []

    # Se hace una listas de listas, en las que cada lista equivale a una fila de la matriz
    for n in range(row):
        aux = []
        for m in range(column):
            aux.append(
                int(input(f'Digite el número de la posición {n}, {m} de la matriz: ')))
        matrix.append(aux)

    print(f'\nLa matriz creada es la siguiente:\n{np.asmatrix(matrix)}\n')
    return np.asmatrix(matrix)

# Método para el producto escalar de un entero y una matriz
def pointMatrix(escalar, original_matrix):
    matrix = original_matrix.copy()
    for n in range(matrix.shape[0]):
        for m in range(matrix.shape[1]):
            matrix[n, m] =matrix[n, m] * escalar
    print(f'{matrix}\n')

# Método para la suma de dos 
def sumMatrix(matrix1, matrix2):
    if(matrix1.shape == matrix2.shape):
        matrix = np.zeros((matrix1.shape[0], matrix1.shape[1]))
        for n in range(matrix.shape[0]):
            for m in range(matrix.shape[1]):
                matrix[n, m] = matrix1[n, m] + matrix2[n, m]
        print(f'{matrix}\n')
    else:
        print('Las matrices no coinciden en tamaño, no se puede realizar la suma')

# Definir tamaños
rows1 = int(input('Defina las filas de la matriz 1: '))
columns1 = int(input('Defina las columnas de la matriz 1: '))

rows2 = int(input('Defina las filas de la matriz 2: '))
columns2 = int(input('Defina las columnas de la matriz 2: '))

# Digitar datos con el método para llenar la matriz
print('\nDigitado de datos de la matriz 1\n\n')
matrix1 = fillMatrix(rows1, columns1)

print('\n\nDigitado de datos de la matriz 2\n\n')
matrix2 = fillMatrix(rows2, columns2)

# Imprimir la matriz
print(f'Matriz A: \n {matrix1}\n')
print(f'Matriz B: \n {matrix2}\n')

# Operación 3A
print('Matriz 3A: ')
pointMatrix(3, matrix1)

# Operación 4B
print('Matriz 4B: ')
pointMatrix(4, matrix2)

# Operación A + B
print('Matriz A+B: ')
sumMatrix(matrix1, matrix2)

# Operación B x A
print('Matriz  BxA: ')
try:
    print(np.cross(matrix2, matrix1))
except:
    print('Las matrices no cumplen con las condiciones para poder realizar el producto vectorial')