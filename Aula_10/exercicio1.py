num = 0
maior = 0.3
menor = 2.3
alunomaior = num
alunomenor = num

for cont in range(10):
    num = int(input("Qual seu número de aluno? "))

    alt = float(input("Qual sua altura? "))

    if alt > maior:
        maior = alt
        alunomaior = num

    if alt < menor:
        menor = alt
        alunomenor = num

print(f"O maior aluno é o que tem o número: {alunomaior}")
print(f"Sua altura é: {maior}")
print(f"O menor aluno é o que tem o número: {alunomenor}")
print(f"Sua altura é: {menor}")
