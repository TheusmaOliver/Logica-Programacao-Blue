def func(x):
    print("x é: ", x)
    x = 2
    print("Valor local alterado de x para: ", x)


x = 50
func(x)
print("x ainda é: ", x)


def func():
    global x
    x = 19  # Aqui esta sendo alterado o objeto x global
    y = x*2
    print("X global existe dentro da função: valor = {0}".format(x))
    print("Y local existe dentro da função: valor = {0}".format(y))


print("Inicio do programa")
x = 10
print("X global existe fora da função: valor = {0}".format(x))
func()
print("X global alterado na função: valor = {0}".format(x))
print("Fim do programa")
print()


def maior(x, y):
    if x > y:
        return x
    else:
        return y


print(maior(7, 8))
