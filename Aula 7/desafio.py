# Desafio


def custo_hotel(noites):
    custo = noites * 140
    return custo


def custo_aviao(cidade):
    if cidade == 'São Paulo' or cidade == "Sao Paulo":
        custo = 312
        return custo
    elif cidade == 'Porto Alegre':
        custo = 447
        return custo
    elif cidade == 'Recife':
        custo = 831
        return custo
    elif cidade == 'Manaus':
        custo = 986
        return custo
    else:
        return 0


def custo_carros(dias):
    custo = 40
    desconto_3dias = 20
    desconto_7dias = 50
    custoCarroTotal = dias * custo

    if dias >= 7:
        custoCarroTotal -= desconto_7dias
    elif dias >= 3:
        custoCarroTotal -= desconto_3dias

    return custoCarroTotal


def custo_total(noites, cidade, dias, gasto_extras):
    total = custo_hotel(noites) + custo_aviao(cidade) + \
        custo_carros(dias) + gasto_extras
    return total


noites = int(input("Digite quantas noites quer ficar no hotel: "))
cidade = input("Digite para qual cidade quer ir: ")
dias = int(input("Digite quantos dias quer alugar um carro: "))
gasto_extras = float(input("Gastos extras: "))

print(f'O valor do hotel é: R$ {(custo_hotel(noites))}')
print(f'O valor da passagem é: R$ {custo_aviao(cidade)}')
print(f'O valor do aluguel de carros é: R$ {custo_carros(dias)}')
print(f'Gastos extras: R${gasto_extras}')
print(
    f'O custo total da viagem é: R$ {custo_total(noites, cidade, dias, gasto_extras)}')
