opc2 = 1
opc = 1
while opc == 1:
    num = 1
    cont = 1

    qtd = int(input("Digite a quantidade de números impares desejado: "))
    números = []
    while cont <= qtd:
        print(num)
        números.append(num)
        cont = cont + 1
        num = num + 2
    print()
    print("Tamanho da lista: ", len(números))
    print()
    print("Lista: ", números)
    print()
    for cont in números:
        sort = sorted(números, reverse=True)
    aux = len(números)

    for i in range(aux, 1, 1):
        print(números[aux])
    resp = input("Você deseja continuar (S/N)?").upper()

    while resp != 'S' and resp != 'N':
        resp = input("Resposta inválida, Deseja continuar? (S/N) ").upper()
    while resp == 'N':
        print('Fim do Programa!')
        opc = 0
        resp = ''
