from datetime import date


def verifica(date):
    global day
    global year
    global atual
    global indexMonth

    meses = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro']
    month = meses[indexMonth]

    if (len(date) < 10 and len(date) > 10):
        print('Null')
        return date
    elif (date[2] != '/' or date[5] != '/'):
        print('Null')
        return date
    elif (indexMonth < 1 or indexMonth > 12):
        print('Null')
        return date
    elif day < 1 or day > 31:
        print('Null')
    elif year > atual:
        print('Null')
    elif month == 'fevereiro' and day > 28 and year % 4 == 1:
        print("Fevereiro so tem 28 dias em anos não bissextos!")
    elif month == 'fevereiro' and day >= 30:
        print('Fevereiro so tem 29 ou 28 dias!')
    elif month == 'abril' and day > 30:
        print('Abril so tem 30 dias!')
    elif month == 'junho' and day > 30:
        print('Junho so tem 30 dias!')
    elif month == 'setembro' and day > 30:
        print('Setembro so tem 30 dias!')
    elif month == 'novembro' and day > 30:
        print('Novembro so tem 30 dias!')
    else:
        print(f'{day} de {month} de {year}')


data = input("Digite uma data (DD/MM/AAAA): ")

day = int(data[0:2])
indexMonth = int(data[3:5])
year = int(data[6:10])
atual = date.today().year

verifica(data)
