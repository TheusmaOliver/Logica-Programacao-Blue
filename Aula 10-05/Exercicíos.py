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

# Exercicío 4


def salario(horasTrabalhadas, valor_hora):
    salario = horasTrabalhadas * valor_hora
    print("Você irá receber: R$", salario)
    if horasTrabalhadas > 40:
        hextra = horasTrabalhadas - 40
        hextra = hextra * (valor_hora * 1.5)
        salario = salario + hextra
        print("\nO valor da hora extra é: ", hextra)
        print("Você irá receber: R$", salario)


valor_hora = float(input("Quanto você recebe por hora? \n"))
horasTrabalhadas = float(input("\nQuantas horas você trabalho? \n"))
salario(horasTrabalhadas, valor_hora)

# Exercicío 5


def IMC(altura, peso):
    imc = peso / altura**2
    print("Seu imc é: %.2f" % imc)


altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

IMC(altura, peso)

# Exercucío 6


def conversor(nota):
    if nota >= 9.0:
        print("A")
    elif nota >= 8.0:
        print("B")
    elif nota >= 7.0:
        print("C")
    elif nota >= 6.0:
        print("D")
    elif nota >= 4.1:
        print("E")
    elif nota <= 4.0:
        print("F")


nota = float(input("Digite sua nota: "))

conversor(nota)

# Exercicío 7


def numeros(numero1, numero2):
    min = numero1

    if numero2 < min:
        min = numero2
        print("O menor número é: ", min)
    elif numero1 == numero2:
        print("Números iguais")
    else:
        min = numero1
        print("O menor número é: ", min)


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

numeros(n1, n2)
