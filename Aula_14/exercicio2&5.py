# Resolução exercicio 2 e 5

def verificaVogais(frase):
    vogais = 0
    for letra in frase:
        if letra in "aeiou":
            vogais += 1
    return vogais


def retornaFrase(frase):
    resposta = ''
    for letra in frase:
        if letra not in 'aeiou':
            resposta += letra
    return resposta


frase = input("Digite uma frase: ").lower()

print(f'O resultado da frase "{retornaFrase(frase)}".')
print(f'Foram retiradas {verificaVogais(frase)} letras.')
