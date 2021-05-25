import math

# Se pide x en: e^-x
valor = int(input('Digite x en e^-x: '))

# Definiciones
error_esperado = ((0.5 * math.pow(10, -7)) * 100)
error_relativo = 100
iteraciones = 0
potencia = 0
x = 0
y = 0
z = 0


# Bucle infinito
while True:

    # Mientras el error esperado sea menor que el error relativo
    if(error_esperado<error_relativo):

        # Por cada iteración, se almacena la sucesión en z y x almacena 1 / z
        y = x
        z = z + (math.pow(valor, potencia)/math.factorial(potencia))
        x = 1/z
        iteraciones += 1
        potencia += 1


        # Calcular el error relativo
        error_relativo = abs((x - y )/x) * 100

        # Imprimir iteración realizada, valor de la iteración y error relativo de la iteración
        print('-' * 20)
        print(f'La iteración actual es: {iteraciones}')
        print(f'El valor de la iteracion actual es: {x}')
        print(f'Su error relativo es: {error_relativo}')
        print('-' * 20)
        print('\n' * 3)

    # Terminar la ejecución del programa, imprimir la última iteración, el valor y su error relativo
    else:
        print('\n' * 3)
        print('-' * 20)
        print(f'La iteración final es: {iteraciones}')
        print(f'El valor de la iteracion final es: {x}')
        print(f'Su error relativo es: {error_relativo}')
        print('-' * 20)
        exit(0)