# Exercucío 6


def conversor(nota):
    if nota >= 9.0:
        print("A")
    elif nota >= 8.0:
        print("B")
    elif nota >= 7.0:
        print("C")
    elif nota >= 6.0:
        print("D")
    elif nota >= 4.1:
        print("E")
    elif nota <= 4.0:
        print("F")


nota = float(input("Digite sua nota: "))

conversor(nota)
