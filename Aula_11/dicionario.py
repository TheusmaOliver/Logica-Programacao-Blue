contatos_lista = [("Gustavo", '1234-5678'), ("Paulo", '9999-8888'),
                  ("Jaque", '8765-3456'), ("Laura", '7788-8877')]

print(contatos_lista[2][0], contatos_lista[2][1])

# Para criar dicionários utiliza-se {} ou a funçao dict()
# Para lista usamos []


contatos = dict(contatos_lista)

print(contatos["Gustavo"])

# Metodo Get -> buscar valores em dicionarios pela Key (Chave)

print()
print(contatos.get('Chuck Norris', 'Contato não encontrado'))

print('7788-8877' in contatos.values())

print('-='*50)

print('Adicionando contatos no dicionario')
print()

contatos['Mulher Maravilha'] = '2233-9765'

# Adicionando com input - Forma 1
'''a = input("Digite um nome: ")
b = input("Digite o telefone: ")

contatos[a] = b
print()

# Adicionando com input - Forma 2
contatos[input("digite a chave: ")] = input("Digite o valor: ")

print(contatos)'''

print()
print('-='*50)
print("Removendo contatos no dicionario")
print()

# usando pop

print(contatos.pop('Deadpool', 'Contato não encontrado'))

print(contatos)

print('-='*50)
print('Unindo dicionários')
print()

contatos_matheus = [('Yago', '1234-5679'), ('Maicon', '9999-8887'),
                    ('Thiago', '8765-3455'), ('Gabriel', '7788-8876')]
contatos2 = dict(contatos_matheus)

for nome in contatos2:
    contatos[nome] = contatos2[nome]

print(contatos)
print()
contatos.update(contatos2)
print(contatos)
print()

contatos3 = {
    "contatos_gustavo": contatos,
    "contatos_matheus": contatos2
}

print(contatos3)
