# Desafio 1

for cont in range(1000, 10000):
    primeiro = cont // 100
    segundo = cont % 100

    resultado = primeiro + segundo
    resultado = resultado ** 2

    if resultado == cont:
        print(f'{cont} - verdadeiro')
