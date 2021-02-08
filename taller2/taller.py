# A tener en cuenta: A efectos del curso el 0 o 1 no son números naturales

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

for i in range(6, 25):
    conjunto_a.add(i)

print(f'Conjunto A: {conjunto_a}\n\n\n')

# Conjunto B
conjunto_b = set()

for i in range(1, 31):
    if(i%2==1):
        conjunto_b.add(i)

print(f'Conjunto B: {conjunto_b}\n\n\n')

# Conjunto C
conjunto_c = set()

conjunto_c = {0, 3, 6, 9, 11, 15, 18, 20}

print(f'Conjunto C: {conjunto_c}\n\n\n')

# Conjunto D
conjunto_d = set()

for i in range(1, 40):
    aux = numero_primo(i)
    if(aux):
        conjunto_d.add(i)

print(f'Conjunto D: {conjunto_d}\n\n\n')

# (A diferencia simétrica B) n C
print(f'(A diferencia simétrica B) n C: {interseccion(diferencia_simetrica(conjunto_a, conjunto_b), conjunto_c)}')

# (A diferencia C) u B
print(f'(A diferencia C) u B: {union(diferencia(conjunto_a, conjunto_c), conjunto_b)}')

# A diferencia simétrica (C u D)
print(f'A diferencia simétrica (C u D): {diferencia_simetrica(conjunto_a, union(conjunto_c, conjunto_d))}')

# (C - A) diferencia simétrica (B n D)
print(f'(C - A) diferencia simétrica (B n D): {diferencia_simetrica(diferencia(conjunto_c, conjunto_a), interseccion(conjunto_b, conjunto_d))}')