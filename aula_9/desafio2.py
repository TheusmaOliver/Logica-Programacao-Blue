
# Desafio 2

materias = int(input("Quantas matérias existe? "))

notas = []

for cont in range(materias):
    nota = float(input(f"Qual nota você tirou na {cont+1} materia? "))
    notas.append(nota)


print(f'{(sum(notas)/materias):.2f}')
