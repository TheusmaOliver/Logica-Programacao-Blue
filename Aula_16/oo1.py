# Classe -> Molde para criar os nossos objetos
# Objetos -> Instâncias da minha classe (funcional)
# Atributos -> Características dos objetos
# Métodos -> Ações que os objetos executam

# Classe: Herói
# Objeto: Capitão América
# Atributos: Nome, idade, peso, altura
# Métodos: Engordar

class Herói():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def engordar(self, peso):
        self.peso += peso


heroi = Herói('Capitão América', 30, 85, 1.90)

print(type(heroi))

for cont in vars(heroi):
    print(cont)

if __name__ == '__main__':
    print("f")
