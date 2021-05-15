print(" [1] - Joazinho\n",
      "[2] - Leozinho\n",
      "[3] - Mariazinha\n",
      "[4] - Gabrielzinho\n",
      "[5] - Voto Nulo\n",
      "[6] - Voto em Branco")

voto = 1
Joazinho = 0
Leozinho = 0
Mariazinha = 0
Gabrielzinho = 0
nulo = 0
branco = 0
total = 0

while voto != 0:
    voto = int(input("Digite o seu voto: "))
    if voto == 1:
        Joazinho += 1
        total += 1
    elif voto == 2:
        Leozinho += 1
        total += 1
    elif voto == 3:
        Mariazinha += 1
        total += 1
    elif voto == 4:
        Gabrielzinho += 1
        total += 1
    elif voto == 5:
        nulo += 1
        total += 1
    elif voto == 6:
        branco += 1
        total += 1

print("\n O total de votos para cada candidato: \n",
      f"Joazinho - {Joazinho}\n",
      f"Leozinho - {Leozinho}\n",
      f"Mariazinha - {Mariazinha}\n",
      f"Gabrielzinho - {Gabrielzinho}\n")

print(" O total de votos nulos: \n",
      f"Votos nulos: {nulo}\n")

print(" O total de votos em branco: \n",
      f"Votos branco: {branco}\n")

print("A porcentagem de votos nulos sobre o total de votos: \n",
      f"Porcentagem: {((nulo/total)*100):.2f} %\n ")

print("A porcentagem de votos brancos sobre o total de votos: \n",
      f"Porcentagem: {((branco/total)*100):.2f} %")
