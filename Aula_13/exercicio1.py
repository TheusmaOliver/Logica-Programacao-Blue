# Exercicio 1


estoque = {'Pao': [10, 0.50],
           'Salgado': [20, 0.30],
           'Pao de queijo': [30, 0.20]}

valorTotal = 0
totalProdutos = 0
produtos = []
nome_produto = []
while True:
    produto = input("Qual produto você deseja? ")

    if produto in estoque:
        print()
        print('======Em estoque=====')
        print()
        print(f'O {produto} custa R$ {estoque[produto][1]}')
        print()
        qtd = int(input("Quantas quantidades: "))
        print()
        if estoque[produto][0] < qtd:
            print("Não temos essa quantidade em estoque.")
        else:
            preco = estoque[produto][1]
            resultado = qtd * preco
            print(f'R$ {resultado:.2f}')
            valorTotal += resultado
            totalProdutos += qtd
            estoque[produto][0] -= qtd
            produtos = qtd
            nome_produto = produto

    else:
        print('=====Sem Estoque=====')

    if input("Você deseja comprar mais produtos? ") in "Nn":
        print('='*40)
        break
    else:
        continue

print(
    f'Você comprou {totalProdutos} produtos, o valor total foi R$ {valorTotal}')
