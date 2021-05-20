
jogo = {}
totalGols = 0

while True:
    nome = input("Digite o nome do jogador: ")
    qtdPartidas = int(input("Digite quantas partidas o jogador jogou: "))
    print()

    qtdGols = [int(input(
        f'Quantos gols o jogador fez na {cont+1}° partida? ')) for cont in range(qtdPartidas)]
    print()
    jogo[nome] = qtdGols
    totalGols += sum(qtdGols)

    v = 0
    for cont in range(len(qtdGols)):
        v += 1
        print(f'Na {v}° partida o jogador {nome} fez {qtdGols[cont]} gols')
    print()
    if input("Deseja cadastrar mais um jogador? ") in "Nn":
        break

    else:

        continue
print()
for key, value in jogo.items():
    print(f"O jogador {key} fez {sum(value)} gols no campeonato.")
