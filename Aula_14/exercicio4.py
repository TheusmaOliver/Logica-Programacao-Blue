
def transform(date):
    global indexMonth

    meses = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro']
    month = meses[indexMonth]

    return month


def verifica(date):
    global day
    global year
    if (len(date) < 10 and len(date) > 10):
        print('Null')
        return date
    elif (date[2] != '/' or date[5] != '/'):
        print('Null')
        return date
    elif (indexMonth < 1 or indexMonth > 12):
        print('Null')
        return date
    else:
        print(f'{day} de {transform(date)} de {year}')


date = input("Digite uma data (DD/MM/AAAA): ")

day = int(date[0:2])
indexMonth = int(date[3:5])
year = int(date[6:10])


verifica(date)
