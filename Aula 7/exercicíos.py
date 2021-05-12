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

# Exercicío 3


def maiusculo(mensagem):
    return mensagem.upper()


mensagem = input("Digite uma mensagem: ")

print(maiusculo(mensagem))

# Exercicio 4


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'{idade} anos: VOTO NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade} anos: VOTO OPCIONAL.'
    else:
        return f'{idade} anos: VOTO OBRIGATÓRIO.'


nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))

# Exercicío 5


def ficha(nome, gols):
    print(f'{nome}, {gols} gols')
    if nome == '' or gols == '':
        print(f'{nome}, {gols} gols')


nome = input("Digite o nome do jogador: ")
gols = input("Digite o número de gols: ")

ficha(nome, gols)

# Exercicío 6


def maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    if n3 >= n1 and n3 >= n2:
        return n3


def menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    if n2 <= n1 and n2 <= n3:
        return n2
    if n3 <= n1 and n3 <= n2:
        return n3


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
print('A média original é:{:.2f}'.format((n1+n2+n3)/3))
print('A média das duas melhores é:{:.2f}'.format(
    ((n1+n2+n3)-menor(n1, n2, n3))/2))

print('A maior nota foi:', maior(n1, n2, n3))
print('A nota menor foi:', menor(n1, n2, n3))
