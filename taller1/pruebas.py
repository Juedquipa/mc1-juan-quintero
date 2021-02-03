# Conjunto 1
aux0 = int(input("Escriba el tamaño del conjunto A: "))
hashset0 = set()

for i in range(aux0):
    aux1 = int(input(f'Escriba el número en la posición {i} de la lista: '))
    hashset0.add(aux1)

print(f'\n\nConjunto A = {hashset0}')

# Conjunto 2
aux0 = int(input("Escriba el tamaño del conjunto B: "))
hashset1 = set()

for i in range(aux0):
    aux1 = int(input(f'Escriba el número en la posición {i} de la lista: '))
    hashset1.add(aux1)

print(f'\n\nConjunto B = {hashset1}')

# Conjunto unión
print(f'\n\nConjunto A U B = {hashset0 | hashset1}')
print(f'Su cardinalidad es de {len(hashset0 | hashset1)}\n\n')

# Conjunto intersección
print(f'Conjunto A n B = {hashset0 & hashset1}')
print(f'Su cardinalidad es de {len(hashset0 & hashset1)}\n\n')

# Conjunto A - B
print(f'Conjunto A - B = {hashset0 - hashset1}')
print(f'Su cardinalidad es de {len(hashset0 - hashset1)}\n\n')

# Conjunto B - A
print(f'Conjunto B n A = {hashset1 - hashset0}')
print(f'Su cardinalidad es de {len(hashset1 - hashset0)}\n\n')

# Conjunto diferencia simétrica
print(f'Conjunto A diferencia simétrica B = {hashset0 ^ hashset1}')
print(f'Su cardinalidad es de {len(hashset0 ^ hashset1)}\n\n')
