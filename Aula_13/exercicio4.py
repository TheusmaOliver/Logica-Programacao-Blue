celebridades = {'Daniel Radcliffe': '23/07/1989',
                'Emma Watson': '15/04/1990',
                'Robert Downey Jr.': '04/04/1965',
                'Chris Evans': '13/06/1981',
                'Chris Hemsworth': '11/08/1983'}
print()

while True:
    for k, v in celebridades.items():
        print(f'{k}')
    print()

    nome = input("De quem você gostaria de saber a data de nascimento? ")
    print()

    if nome in celebridades:
        print(
            f'Data de nascimento da celebridade {nome}: {celebridades.get(nome)}')
        print()
    else:
        print("Não sabemos a data de nascimento dessa celebridade.")
        print()

    if input("Deseja saber a data de nascimento de outra celebridade? ") in 'Nn':
        print()
        break
    else:
        print()
        continue
