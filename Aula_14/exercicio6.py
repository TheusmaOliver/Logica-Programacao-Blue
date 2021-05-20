perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ",
             "Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]

respostas = []
sim = 0
for cont in perguntas:
    resp = input(cont)
    respostas.append(resp)
    if resp == 'sim':
        sim += 1

classificacao = ["Inocente", "Suspeita", "Cúmplice", "Assassino"]
print()
if sim == 2:
    print(classificacao[1])
elif 3 <= sim <= 4:
    print(classificacao[2])
elif sim == 5:
    print(classificacao[3])
else:
    print(classificacao[0])
