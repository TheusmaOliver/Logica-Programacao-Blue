# Exercicío 6

preco_pao = float(input("Digite o valor do pão: "))


for cont in range(1, 51):

    print(f'{cont} - R$ {(cont * preco_pao):.2f}')
