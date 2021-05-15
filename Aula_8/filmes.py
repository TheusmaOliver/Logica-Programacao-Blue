filmes = ['Os Vingadores', 'HP', 'Forrest Gump', 'A Procura da Felicidade',
          'Como eu era antes de você', 'O lobo de Wall Street', 'Dois Coelhos', 'UP', 'Lagoa Azul']
filmes.append('Power Rangers')
print(filmes)
print()
filmes_novos = ['Histórias Cruzadas', 'Esqueceram de mim', 'Desventuras em Série', 'Poderoso Chefão',
                'De volta para o futuro', 'Ben Hur']
filmes.extend(filmes_novos)

print(filmes)
print()
filmes.sort()
print(filmes)
print()
filmes.reverse()
print(filmes)
print()

filmes.insert(1, "Pianista")
filmes.insert(10, "Projeto X")
filmes.sort()
print(filmes)

filmes.remove('HP')
print()
print(filmes)

filmes.remove('Desventuras em Série')
print()
print(filmes)

filmes.pop(8)
filmes.pop()
filmes.pop()
del filmes[1]
# del filmes[:] - Apaga a Lista toda
del filmes[0:4]

for filme in filmes:
    print()
    print(filme)

print()
print(len(filmes))
