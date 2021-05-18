dict = {1: 1, 4: 4, 5: 5, 6: 6, 7: 7, 9: 9}

for i, v in dict.items():
    dict[i] = v**2


print(dict)

chaves = [1, 4, 5, 6, 7, 9]
dict2 = {}

for cont in chaves:
    dict2[cont] = cont**2

print(dict2)
