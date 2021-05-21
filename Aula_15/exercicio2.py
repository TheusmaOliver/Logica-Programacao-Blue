numeros = []

while True:
    numero = float(input("Digite qual número deseja (0 para sair): "))
    numeros.append(numero)

    if numero == 0:
        numeros.pop()
        break
    else:

        continue
print()
print(f"foram digitados {len(numeros)} números.")
print()
numeros.sort(reverse=True)
print("Lista ordenada de forma decrescente:")
for cont in numeros:
    print(cont)
print()
if 5 in numeros:
    print("O número 5 foi digitado e está na lista")
else:
    print("O número 5 não foi digitado")
