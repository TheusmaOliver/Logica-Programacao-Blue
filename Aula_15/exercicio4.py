def contagem(i, f, p):
    print('-='*10)
    print(f'Contagem de {i} até {f} passo {p}')
    print()
    for num in range(i, f, p):
        print(num, end=' ')
    print('FIM')


contagem(1, 10, 1)

contagem(10, -1, -2)
print('-='*10)
print('Personalize a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)
