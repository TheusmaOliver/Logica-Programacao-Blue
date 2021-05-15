# Exercicío 1

def numeros(n1, n2):
    min = n1
    if n2 < min:
        min = n2
        print("o menor número é: ", min)
    elif n1 == n2:
        print("Valores idênticos")
    else:
        print("o menor número é: ", min)


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

numeros(n1, n2)
