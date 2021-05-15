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
