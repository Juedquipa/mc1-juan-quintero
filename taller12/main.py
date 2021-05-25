import math
import numpy as np
import sympy

# Definir X como variable en una función
x = sympy.Symbol('x')

# Definir la función a la que se le hará la serie de Taylor
function = math.e**-x

# Definir variables
value = 0
count = 0
error = 0
last_f_prime = function

# Definir la base y el punto
point = 0.755
base = 0.75

# Definir valor esperado
expected = function.subs(x, point)

# Serie de taylor
def taylor(value, count, function, last_f_prime, point, base):

    # En la primera iteración solo evaluar la función
    if (count==0):
        value1 = last_f_prime.subs(x, base)
        return value1, last_f_prime

    # En las demás iteraciones evaluar el resto
    else:
        fprime = last_f_prime.diff()
        value1 = value + ( ( (fprime.subs(x, base)) / (math.factorial(count)) ) * math.pow(point - base, count) )
        return value1, fprime

# Calcular el error relativo
def relativeError(va, ve):
    
    error = abs((va-ve)/ve)*100
    return error

# Main
for i in range(0, 16):
    
    value, last_f_prime = taylor(value, count, function, last_f_prime, point, base)
    count = count + 1
    error = relativeError(value, expected)
    
    print(
        "----------------------" +
        f"\nIteración {count}" +
        f"\nValor obtenido: {value}" +
        f"\nValor esperado: {expected}" +
        f"\nError relativo porcentual: {error}" +
        "\n----------------------"
    )
