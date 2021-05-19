from operator import itemgetter
import random
import time

jogadores = []

for cont in range(4):
    jogador = input("Digite seu nome: ")
    jogadores.append(jogador)
print()
print('='*40)

resultado = {}
for cont in jogadores:
    numeros = random.randint(1, 6)
    print(f'O jogador {cont} tirou {numeros} no dado')
    time.sleep(2)
    resultado[cont] = numeros
print()
print('   ====RANKING====')
print()

ordem = sorted(resultado.items(), key=itemgetter(1), reverse=True)

for i, cont in enumerate(ordem):
    print(f'{i+1}º lugar: {cont[0]} com {cont[1]}.')
    time.sleep(2)
