import numpy as np
import copy

# Hacer la diagonal principal y la parte de abajo de la matriz identidad
def gaussJordan(matrix):
    n = 0
    while True:
        # Cuando se termine el proceso, n será mayor que la longitud de la matriz
        if(n >= len(matrix)):
            return matrix

        # Si la diagonal es 0, se cambia de posición con otra fila
        if(matrix[n][n] == 0):
            isZero(matrix, n)
            print(
                f'\nSe cambiaron las filas de la matriz: \n{np.asmatrix(matrix)}')

        # Si la diagonal es uno, se restan las filas para que se cree la matriz identidad
        elif(matrix[n][n] == 1):
            subsAll(matrix, n)
            print(f'\nSe restaron filas de la matriz: \n{np.asmatrix(matrix)}')
            n += 1

        # Cuando la diagonal no sea 1 o 0, se divide la fila para poder crear la fila con la diagonal 1
        else:
            divideAll(matrix, n)
            print(
                f'\nSe dividió una fila de la matriz: \n{np.asmatrix(matrix)}')

# Método para cambiar de posición las ecuaciones en caso de que el número en la diagonal principal sea 
def isZero(matrix, aux1):
    aux2 = 0
    while True:

        # Si no se puede resolver por Gauss Jordan, salta error
        if(aux2 >= len(matrix)-1):
            print(
                f'La última iteración de la matriz fue: \n{np.asmatrix(matrix)}')
            raise IndexError('No se puede resolver el sistema por GaussJordan')

        # Mover las filas por un auxiliar
        aux0 = matrix[aux2+1]
        matrix[aux2+1] = matrix[aux2]
        matrix[aux1] = aux0

        # Si sigue siendo cero, que siga el bucle infinito
        if (matrix[aux1][aux1] != 0):
            return matrix
        aux2 += 1

# Método para dividir toda una fila y establecer el número de la diagonal principal como 1
def divideAll(matrix, n):
    aux0 = 0
    aux1 = matrix[n][n]
    for number in matrix[n]:
        matrix[n][aux0] = number / aux1
        aux0 += 1
    return matrix

# Método para restar una fila que ya tenga su número de diagonal principal como 1 con las otras filas
def subsAll(matrix, n):
    aux0 = 0
    while True:
        for row in range(len(matrix)):

            # Si la columna a evaluar es si misma, saltarse ese paso
            if(row != n):

                # Si ambos numeros son iguales, se restan la filas para que quede 0
                if(matrix[n][n] == matrix[row][n]):
                    for number in range(len(matrix[n])):
                        matrix[row][number] = matrix[row][number] - \
                            matrix[n][number]

                # Si un número en una fila ya es cero, se le suma a un iterador, si todas los números correspondientes son cero, acaba el método
                elif(matrix[row][n] == 0):
                    aux0 += 1
                    if(aux0 == len(matrix)):
                        return matrix

                # Si no es cero, pero tampoco es 1, multiplica la fila con el número correspondiente de la columna y después lo resta
                else:
                    aux1 = copy.deepcopy(matrix)
                    for number in range(len(matrix[n])):
                        aux1[n][number] = aux1[n][number] * aux1[row][n]
                    for number in range(len(matrix[n])):
                        aux1[row][number] = aux1[row][number] - aux1[n][number]
                    for number in range(len(matrix[n])):
                        matrix[row][number] = aux1[row][number]


# Definir la matriz
matrix = [[0, 1, 1, 3], [4, 4, 7, 26], [0, 1, 2, 12]]

# Mostrar la matriz inicial
print(f'La matriz inicial es: \n{np.asmatrix(matrix)}')

gaussJordan(matrix)
print(f'\n\n\n\nLa matriz resuelta es: \n{np.asmatrix(matrix)}')