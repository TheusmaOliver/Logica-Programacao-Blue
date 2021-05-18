opc = True

while opc == True:
    senha = input("Digite a senha: ")

    while senha != 'paodeforma':
        print("Senha inválida!")
        senha = input("Digite a senha:")
    if senha == 'paodeforma':
        opc = False

print("Programa finalizado! ")
