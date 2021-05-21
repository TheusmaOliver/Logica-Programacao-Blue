from random import randint

print("Seja bem vindo ! vamos iniciar seu cadastro abaixo ")

usuario = input("informe seu nome de usuário para cadastro:")
senha = input("Informe uma senha para cadastro:")

while usuario == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

print("Cadastro aprovado")

login = input("informe o seu nome de usuário: ")

while login != usuario:
    print("Login incorreto, tente novamente!")
    login = input("Informe o seu nome de usuário: ")

sen = input("Informe a sua senha: ")


while sen != senha:
    print("Senha incorreta, tente novamente: ")
    sen = input("Informe a sua senha: ")

print("Bem vindo ao jogo da adivinhação! será que você consegue adivinhar o número que eu estou pensando ?!")
computador = randint(0, 10)


print("Vou pensar num número de 0 a 10, tente adivinhar !")

acertou = False
acertou = 0

while not acertou:
    jogador = int(input("E aí, qual o seu palpite ? ( de 0 a 10): "))

    if jogador == computador:
        acertou = True
        print(f"Você acertou !!! eu pensei exatamente no número {computador}")
    else:
        if jogador < computador:
            print(
                f"Hmm... não foi dessa vez, eu pensei num número maior que {jogador}")
        elif jogador > computador:
            print(
                f"Hmm... não foi dessa vez, eu pensei num número menor que {jogador}")
