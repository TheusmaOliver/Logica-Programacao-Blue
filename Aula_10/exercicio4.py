opc = 1

while opc == 1:
    palavra = input("Digite a palavra correta: ")

    while palavra != "computador":
        print()
        print("Palavra incorreta!")
        print()
        palavra = input("Digite a palavra correta: ")

    if palavra == "computador":
        print()
        opc = 0
        print("Palavra correta!")
