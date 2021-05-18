vingadores = {'Iron Man': 'Robert Downey', 'Captain America': 'Chris Evans', 'Black Widow': 'Scarlett Johansson', 'Thor': 'Chris Hemsworth',
              'Hulk': 'Mark Ruffalo', 'Nick Fury': 'Samuel L Jackson', 'Vision': 'Paul Bettany', 'Antman': 'Paul Rudd', 'God': 'Stan lee'}

vingadores_lista = ['Miranha', 'Lóqui', 'Tãnuz', 'Bátima']
print()
for k, v in vingadores.items():
    print(f'{k} - {v}')


for i, v in enumerate(vingadores_lista):
    print(i + 1, v)
