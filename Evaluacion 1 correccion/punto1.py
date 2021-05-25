# Diferencia simétrica entre a y b
def diferencia_simetrica(conjunto_a, conjunto_b):
    hashset = set()
    hashset = conjunto_a ^ conjunto_b
    return hashset

# Unión entre a y b
def union(conjunto_a, conjunto_b):
    hashset = set()
    hashset = conjunto_a | conjunto_b
    return hashset

# Intersección entre a y b
def interseccion(conjunto_a, conjunto_b):
    hashset = set()
    hashset = conjunto_a & conjunto_b
    return hashset

# Diferencia entre a y b
def diferencia(conjunto_a, conjunto_b):
    hashset = set()
    hashset = conjunto_a - conjunto_b
    return hashset

# Números Primos
def numero_primo(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             

# Conjunto A

conjunto_a = set()

for i in range(20):
    conjunto_a.add(i+10)

print(f'\n\nConjunto A = {conjunto_a}')

# Conjunto B

conjunto_b = set()
conjunto_b = {0, 2, 4, 6, 12, 24, 48}

print(f'\n\nConjunto B = {conjunto_b}')

# Conjunto C

conjunto_c = set()

for i in range(0 ,46):
    if (i%4==2):
        conjunto_c.add(i)

print(f'\n\nConjunto c = {conjunto_c}')

# Conjunto D

conjunto_d = set()

for i in range(1, 40):
    aux = numero_primo(i)
    if(aux):
        conjunto_d.add(i)

print(f'\n\nConjunto D = {conjunto_d}')

print('-' * 20 + '\n')
# (A-C) dif sim (B n D)

print(f'(A-C) dif sim (B n D): {diferencia_simetrica(diferencia(conjunto_a, conjunto_c), interseccion(conjunto_b, conjunto_d))}')

# ((B n D) dif sim C) - (A u D) 

print(f'((B n D) dif sim C) - (A u D): {diferencia(diferencia_simetrica(interseccion(conjunto_b, conjunto_d), conjunto_c), union(conjunto_a, conjunto_d))}')

# (A n B n C) u ((A-C) u (B-D))

print(f'(A n B n C) u ((A-C) u (B-D)): {union(interseccion(conjunto_a, interseccion(conjunto_b, conjunto_c)), (union(diferencia(conjunto_a, conjunto_c), diferencia(conjunto_b,conjunto_d))))}')
