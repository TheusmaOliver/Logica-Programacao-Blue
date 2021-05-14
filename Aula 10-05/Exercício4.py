# Exercicío 4


def salario(horasTrabalhadas, valor_hora):
    salario = horasTrabalhadas * valor_hora
    print("Você irá receber: R$", salario)
    if horasTrabalhadas > 40:
        hextra = horasTrabalhadas - 40
        hextra = hextra * (valor_hora * 1.5)
        salario = salario + hextra
        print("\nO valor da hora extra é: ", hextra)
        print("Você irá receber: R$", salario)


valor_hora = float(input("Quanto você recebe por hora? \n"))
horasTrabalhadas = float(input("\nQuantas horas você trabalho? \n"))
salario(horasTrabalhadas, valor_hora)
