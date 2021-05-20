numeros = []


for cont in range(7):
    numero = int(input(f"Digite o {cont+1}° numero: "))
    numeros += [numero]
print()

print(numeros)
listaNumeros = []
impares = []

for cont in numeros:
    if cont % 2 == 0:
        listaNumeros += [cont]
    else:
        impares += [cont]
print()

listaNumeros.sort()
impares.sort()

listaNumeros.extend(impares)

print(listaNumeros)
