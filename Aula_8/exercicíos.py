# Exercicío 1
frase = input("Digite uma frase: ").lower()
vogais = 0

for letra in frase:
    if letra in "aeiou":
        vogais += 1

print(f'Existe {vogais} vogais.')

# Exercicío 2


n = 10

for divisor in range(1, n+1):
    if n % divisor == 0:
        print(divisor)

# Exercicío 3

frase = input("Digite uma frase: ")
resposta = ""
for letra in frase:
    if not letra in "aeiouAEIOU":
        resposta += letra

print(resposta)
