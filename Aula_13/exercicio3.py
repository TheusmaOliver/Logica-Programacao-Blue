print(" [0] - Sair\n",
      "[1] - Exibir lista de alunos com suas notas(Cada aluno tem uma nota)\n",
      "[2] - Inserir aluno e nota\n",
      "[3] - Alterar a nota de um aluno\n",
      "[4] - Consultar nota de um aluno específico\n",
      "[5] - Apagar um aluno da lista\n",
      "[6] - Exibir a média da turmar\n")

alunos = {}

while True:
    menu = int(input("Escolha uma opção: "))
    print()

    if menu == 0:
        break
    else:
        if menu == 1 and len(alunos) != 0:
            print("====Lista de alunos====")
            print()

            for k, v in alunos.items():
                print(f'{k} - nota {v}')
            print()

        elif menu == 2:
            aluno = input("Digite o nome do aluno: ")
            nota = float(input("Digite a nota do aluno: "))
            alunos[aluno] = nota
            print()
            print("Aluno registrado!")
            print()

        elif menu == 3 and len(alunos) != 0:
            print("====Lista de alunos====")
            print()

            for k, v in alunos.items():
                print(f'{k} - nota {v}')
            print()

            aluno = input("Qual o nome do aluno que deseja alterar a nota? ")

            if aluno in alunos:
                nota = float(input("Digite a nota alterada: "))
                alunos[aluno] = nota
                print()

                print("Nota alterada")
                print()
            else:
                print("Aluno não registrado!")

        elif menu == 4 and len(alunos) != 0:
            aluno = input("Deseja consultar a nota de qual aluno? ")
            if aluno in alunos:
                verifica = alunos.get(aluno, "Aluno não registrado!")
                print()

                print(f'{aluno} - nota {verifica}')
                print()
            else:
                print("Aluno não registrado!")

        elif menu == 5 and len(alunos) != 0:
            print("====Lista de alunos====")
            print()

            for k, v in alunos.items():
                print(f'{k} - nota {v}')
            print()

            aluno = input("Digite qual aluno deseja apagar: ")
            if aluno in alunos:
                del alunos[aluno]
                print()

                print("Aluno apagado!")
                print()
            else:
                print("Aluno não registrado!")

        elif menu == 6 and len(alunos) != 0:
            soma = 0
            for k, v in alunos.items():
                soma += v

            media = soma / len(alunos)
            print(f"Média da turma: {media:.2f}")
            print()

        else:
            print("Nenhum aluno registrado!")
            print()
