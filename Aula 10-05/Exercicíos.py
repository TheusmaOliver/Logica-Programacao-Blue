# Exercicío 1
def soma(a, b, c):
    print("A soma dos três números é: ", a+b+c)


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma(n1, n2, n3)

# Exercicío 2


def verifica(a):
    if a > 0:
        print("P")
    elif a == 0:
        print(0)
    else:
        print("N")


n1 = int(input("Digite um número: "))
verifica(n1)

# Exercicío 3


def somaImposto(taxaImposto, custo):
    resultado = custo + (custo * taxaImposto / 100)
    return resultado


n1 = float(input("Digite o custo do item: "))
n2 = float(input("Digite o imposto(apenas o número): "))

resultado = somaImposto(n2, n1)
print("O preço com impostos é: ", resultado)
