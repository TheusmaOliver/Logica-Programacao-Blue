dados = {}

nome = input("Digite seu nome: ")
anoNascimento = int(input("Digite o ano do seu nascimento: "))
carteira = int(input("Digite sua carteira de trabalho: "))

dados["Nome"] = nome
dados["Ano"] = anoNascimento
dados["Carteira"] = carteira

if carteira == 0:
    print("Não tem carteira de trabalho!")
else:
    from datetime import date
    anoContratacao = int(input("Digite o ano que foi contratado: "))
    salario = float(input("Digite o seu sálario: "))
    dados["Ano de contratação"] = anoContratacao
    dados["Salário"] = salario
    atual = date.today().year
    idade = atual - anoNascimento
    dados["Idade"] = idade
    aposentadoria = (35 - (2021-anoContratacao))
    dados["Aposentadoria"] = f'Falta {aposentadoria} anos'

print()


for cont in dados:
    print(f'{cont}: {dados[cont]}')
