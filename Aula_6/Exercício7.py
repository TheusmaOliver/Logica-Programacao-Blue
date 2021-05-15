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


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

numeros(numero1, numero2)
