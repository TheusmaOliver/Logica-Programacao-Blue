print()
print("==== Calculadora =====")
print('~-'*14)

numeros = []
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

numeros.append(numero1)
numeros.append(numero2)
print('~-'*14)


print(" [1] - somar\n",
      "[2] - multiplicar\n",
      "[3] - maior\n",
      "[4] - novos números\n",
      "[5] - sair do programa\n")
print('~-'*14)


while True:
    opc = int(input("Digite a opção desejada: "))

    if opc == 1:
        print('~-'*14)

        print(f"A soma dos números é: {sum(numeros)}")

        print('~-'*14)
    elif opc == 2:
        print('~-'*14)

        mult = numeros[0] * numeros[1]
        print(f'A multiplicação dos números é: {mult}')

        print('~-'*14)
    elif opc == 3:
        print('~-'*14)

        print(f'O maior número é: {max(numeros)}')

        print('~-'*14)
    elif opc == 4:
        print('~-'*14)

        numeros.clear()
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))

        numeros.append(numero1)
        numeros.append(numero2)

        print(numeros)

        print('~-'*14)

    if opc == 5:
        break
    else:
        continue
