# Exercicío 5


def IMC(altura, peso):
    imc = peso / altura**2
    print("Seu imc é: %.2f" % imc)


altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

IMC(altura, peso)
