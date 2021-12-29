lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
lista3 = []

#adicionar 2 lista em uma lista princial intercalando as 2 listas
for i in range(len(lista1)):
    lista3.append(lista1[i])
    if True:
        lista3.append(lista2[i])

print(lista3)