opc = True

while opc == True:
    senha = input("Digite a senha: ")
    if senha == 'paodeforma':
        opc = False
    while senha != 'paodeforma':
        print("Senha inválida!")
        senha = input("Digite a senha:")


print("Programa finalizado! ")
