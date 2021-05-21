from datetime import date

dados = {}

nome = input("Digite seu nome: ")
anoNascimento = int(input("Digite o ano do seu nascimento: "))
carteira = int(input("Digite sua carteira de trabalho: "))
print()
atual = date.today().year
idade = atual - anoNascimento

dados['Nome'] = nome
dados['Ano do nascimento'] = anoNascimento
dados['Idade'] = idade

if carteira != 0:
    anoContratacao = int(input("Digite o ano que foi contratado: "))
    anosTrabalhados = int(input("Informe quantos anos você trabalhou: "))
    salario = float(input("Digite seu salário: "))

    aposentadoria = ((35 - anosTrabalhados) + idade)

    dados['Ano do contrato'] = anoContratacao
    dados['Salário'] = salario
    dados['Aposentadoria'] = f'{aposentadoria}'
else:
    print("Sem carteira de trabalho")

print()

for k, v in dados.items():
    print(f'{k}: {v}')
