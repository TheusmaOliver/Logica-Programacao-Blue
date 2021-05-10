print("Funções")
print()

# Definindo uma função


def blue():
    print("E sou um Bluemer")


# Chamando a função
blue()

print()
print("Exemplo de Função com parâmetros")

# Definindo a função


def subtracao(a, b):  # a e b são parâmetros da minha função
    print("A subtração é: ", a-b)


def soma(a, b):
    print("A soma é: ", a+b)


def mult(a, b):
    print("A multiplicação é: ", a*b)


def div(a, b):
    print(f"A divisão é: {a/b:.2f}")


# chamando a função
subtracao(10, 5)
soma(200, 127)
mult(10, 10)
div(40, 6)
