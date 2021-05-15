# Exercicio 3
solteiro = 0
casado = 0

estado = ['solteiro', 'solteiro', 'solteiro', 'solteiro', 'solteiro', 'solteiro',
          'solteiro', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado', 'casado']


for cont in estado:
    if cont == "casado":
        casado += 1
    if cont == "solteiro":
        solteiro += 1

print(f"Existe {solteiro} pessoas solteiras.")
print(f"Existe {casado} pessoas casadas.")
