# Desafio

date = input('Escreva uma data no formato (dia/mês/ano): ')


def calendar(date):

    day = int(date[0:2])
    indexMonth = int(date[3:5])
    year = int(date[6:10])

    month = [
        '', 'janeiro', 'fevereiro',
        'março', 'abril',
        'maio', 'junho',
        'julho', 'agosto',
        'setembro', 'outubro',
        'novembro', 'dezembro'
    ]

    # Tratamento de erros
    if (len(date) < 10 or len(date) > 10):
        print('Null')
    elif (date[2] != '/' or date[5] != '/'):
        print('Null')
    elif (indexMonth < 1 or indexMonth > 12):
        print('Null')

    # Ano bissexto
    if (year % 4 == 0 and year % 100 != 100 or year % 400 == 0):
        print(f'{day} de {month[indexMonth]} de {year} é uma data bissexta')
    else:
        print(
            f'{day} de {month[indexMonth]} de {year} não é uma data bissexta')


calendar(date)
