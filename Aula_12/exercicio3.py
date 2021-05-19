opc = 0
alunos = {}
situacao = {}
qtd = int(input("Quantos alunos? "))

while opc < qtd:
    opc += 1
    nome = input("Digite seu nome: ")
    media = float(input("Digite sua media: "))
    print()

    alunos[nome] = media

    if media >= 7.0:
        situacao[nome] = 'Aprovado'
    elif 5 <= media <= 6.9:
        situacao[nome] = 'Recuperação'
    else:
        situacao[nome] = 'Reprovado'

print('-='*30)

for nome, media in alunos.items():
    print(f'{nome} - {media} - {situacao[nome]}')
