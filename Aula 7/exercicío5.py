# Exercicío 5


def ficha(nome, gols):
    print(f'{nome}, {gols} gols')
    if nome == '' or gols == '':
        print(f'{nome}, {gols} gols')


nome = input("Digite o nome do jogador: ")
gols = input("Digite o número de gols: ")

ficha(nome, gols)
