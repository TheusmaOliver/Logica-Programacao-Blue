# Exercicío 6


def maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    if n3 >= n1 and n3 >= n2:
        return n3


def menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    if n2 <= n1 and n2 <= n3:
        return n2
    if n3 <= n1 and n3 <= n2:
        return n3


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
print('A média original é:{:.2f}'.format((n1+n2+n3)/3))
print('A média das duas melhores é:{:.2f}'.format(
    ((n1+n2+n3)-menor(n1, n2, n3))/2))

print('A maior nota foi:', maior(n1, n2, n3))
print('A nota menor foi:', menor(n1, n2, n3))
