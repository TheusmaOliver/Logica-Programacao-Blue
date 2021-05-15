# Exercicío 8

r1 = input("Telefonou para a vítima[sim/nao]? ")
r2 = input("Esteve no local do crime[sim/nao]? ")
r3 = input("Mora perto da vítima[sim/nao]? ")
r4 = input("Devia para a vítima[sim/nao]? ")
r5 = input("Já trabalhou com a vítima[sim/nao]? ")

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
    print("Inocente")
