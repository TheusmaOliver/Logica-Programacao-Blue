# Exercicío 2


def numeros(a, b, limite):
    if a+b > limite:
        return 'True'
    else:
        return 'False'


limite = 10
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(numeros(a, b, limite))
