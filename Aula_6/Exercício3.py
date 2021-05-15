# Exercicío 3


def somaImposto(taxaImposto, custo):
    resultado = (taxaImposto * custo / 100) + custo
    return resultado


custo = float(input("Digite o custo do item: "))
imposto = float(input("Digite o imposto(apenas o número): "))

resultado = somaImposto(imposto, custo)
print("O preço com impostos é: ", resultado)
