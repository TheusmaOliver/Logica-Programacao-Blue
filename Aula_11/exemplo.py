perguntas = [('nome', 'matheus'), ('idade', '18')]
respostas = [('sexo', 'masculino'), ('altura', '1.80')]

perguntas_dict = dict(perguntas)
respostas_dict = dict(respostas)

for k, v in perguntas_dict.items():
    print(f'{k} - {v}')

for k, v in respostas_dict.items():
    print(f'{k} - {v}')
