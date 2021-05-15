opc = 1
while opc == 1:
    num = float(input("Digite um número: "))

    if num == 0:
        print(f"O número digitado é: {num}")
    elif num > 0:
        print(f"O número {num:.2f} é positivo")
    else:
        print(f"O número {num:.2f} é negativo")
    resp = input("Você deseja finalizar (S/N)? ")
    if resp == 'S':
        opc = 0
        print('Programa finalizado!')
