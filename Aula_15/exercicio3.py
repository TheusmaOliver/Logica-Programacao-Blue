frase = input("Digite uma frase: ").replace(' ', '').lower()

fraseInvertida = frase[::-1]

print(fraseInvertida)
print()

if fraseInvertida == frase:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
