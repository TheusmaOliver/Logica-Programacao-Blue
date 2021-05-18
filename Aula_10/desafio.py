
utilizando = True
gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
notas = []
total_sistema = 0
gabarito_prof = []

for cont in range(10):
    resp = input(
        f"Digite o gabarito da {cont + 1}ª questão:\n").upper().strip()
    gabarito_prof.append(resp)

print(gabarito_prof)

while utilizando == True:
    pontos = 0
    respostas = []
    total_sistema += 1

    for cont in range(1, 11):
        resp_aluno = input(
            f"Digite a resposta da {cont}ª questão:\n").upper().strip()
        respostas.append(resp_aluno)

    for cont in range(10):
        if gabarito_prof[cont] == respostas[cont]:
            pontos += 1

    notas.append(pontos)
    print(f"O aluno acertou {pontos} questões e recebeu uma nota {pontos}.")

    pontos = 0
    respostas = []
    prox_aluno = int(
        input("PRÓXIMO...\nQuer continuar utilizando o sistema?\n[1 - SIM, 0 - NÃO]\n"))

    if prox_aluno == 0:
        utilizando = False

nota_maior = max(notas)
nota_menor = min(notas)
media = sum(notas) / len(notas)
print(f"A maior nota foi {nota_maior} e a nota menor é {nota_menor}.")
print(
    f"O total de alunos que utilizaram o sistemas é de {total_sistema} alunos.")
print(f"A média das notas da turma é de: {media}.")
