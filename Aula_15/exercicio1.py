

numeros = []

for cont in range(5):
    numero = int(input("Digite um número inteiro: "))

    inseriu = False

    for i in range(len(numeros)):
        if numero < numeros[i]:
            numeros.insert(i, numero)
            inseriu = True
            break

    if not inseriu:
        numeros.append(numero)


print(numeros)
