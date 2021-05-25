# Función del producto vectorial
def vectorialProduct(vector1, vector2):
    prod = 0
    # Comprobación
    if(len(vector1) == len(vector2)):
        for n in range(len(vector1)):
            prod += vector1[n] * vector2[n]

        print(f'El producto vectorial es de: {prod}')
    else:
        print('Los vectores no coinciden en tamaño, no se le pueden aplicar el producto vectorial')


# Definición de varialbes y entrada de datos
aux1 = int(input('Escriba el tamaño n de los vectores: '))
vector1 = []
vector2 = []

# Llenado de vector 1
for n in range(aux1):
    aux2 = int(input(f'Digite el número en la posición {n+1} del vector 1: '))
    vector1.append(aux2)

# Llenado de vector 2
for n in range(aux1):
    aux2 = int(input(f'Digite el número en la posición {n+1} del vector 2: '))
    vector2.append(aux2)

vectorialProduct(vector1, vector2)
