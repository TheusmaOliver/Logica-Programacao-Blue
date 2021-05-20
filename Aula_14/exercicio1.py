print("====Exemplo de calculadora=====")

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
print()
soma = numero1 + numero2
mult = numero1 * numero2
divInt = numero1 // numero2
verificaPar = soma % 2

maior = numero1

if numero2 > maior:
    maior = numero2


print(f"O resultado da soma: {soma}")

print(f'O resultado da multiplicação: {mult}')

print(f'A divisão interia: {divInt}')

print(f'O maior entre eles é: {maior}')


if verificaPar == 0:
    print("Resultado da soma é par")
else:
    print("Resultado da soma é impar")

if mult > 40:
    div = mult / divInt
    print(f"O resultado da divisão com a multiplicação maior que 40 é {div}")
else:
    print("A multiplicação não foi maior que 40!")
