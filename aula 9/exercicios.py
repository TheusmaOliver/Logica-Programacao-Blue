
'''# Exercicio 1
tabuada = int(input("Digite um número que quer mostrar a tabuada:"))

for cont in range(11):
    resultado = tabuada * cont
    print(f'{tabuada} X {cont} = {resultado}')

# Exercicio 2

for cont in range(10, 0, -1):
    print(cont)
'''
'''# Exercicio 3
solteiro = 0
casado = 0

estado = ['solteiro', 'solteiro', 'solteiro', 'solteiro', 'solteiro', 'solteiro',
          'solteiro', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado']


for cont in estado:
    if cont == "casado":
        casado += 1
    if cont == "solteiro":
        solteiro += 1

print(f"Existe {solteiro} pessoas solteiras.")
print(f"Existe {casado} pessoas casadas.")

# Exercicio 4

for cont in range(0, 10):
    print("Go Blue")

# Exercicio 5

for cont in range(1, 21, 2):
    print(cont)

preco_pao = float(input("Digite o valor do pão: "))


for cont in range(1, 51):

    print(f'{cont} - R$ {(cont * preco_pao):.2f}')'''

'''r1 = input("Telefonou para a vítima? ")
r2 = input("Esteve no local do crime? ")
r3 = input("Mora perto da vítima? ")
r4 = input("Devia para a vítima? ")
r5 = input("Já trabalhou com a vítima? ")

respostas = [r1, r2, r3, r4, r5]

sim = 0


for cont in respostas:
    if cont == "sim":
        sim += 1

if sim == 2:
    print("Suspeito")
elif sim == 3 or sim == 4:
    print("Cúmplice")
elif sim == 5:
    print("Assassino")
else:
    print("Inocente")'''

for cont in range(1000, 10000):
    primeiro = cont // 100
    segundo = cont % 100

    resultado = primeiro + segundo
    resultado = resultado ** 2

    if resultado == cont:
        print(f'{cont} - verdadeiro')


'''materias = int(input("Quantas matérias existe? "))

notas = []

for cont in range(materias):
    nota = float(input(f"Qual nota você tirou na {cont+1} materia? "))
    notas.append(nota)


print(f'{(sum(notas)/materias):.2f}')
'''
