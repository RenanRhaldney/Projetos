listaDeCaracteres = []
listaDeVogais = []
contador = 0

print('Informe 10 caracteres.')

# adicionar dados na lista
for i in range(10):
    listaDeCaracteres.append(input())
    # verificar se tem consoante ou nao
    if listaDeCaracteres[i] == 'a' or listaDeCaracteres[i] == 'e' \
            or listaDeCaracteres[i] == 'i' or listaDeCaracteres[i] == 'o' or listaDeCaracteres[i] == 'u':
        listaDeVogais.append(listaDeCaracteres[i])
        contador += 1



print('Lista original = ', listaDeCaracteres)
print('Quantidade de vogais =', contador)
print('vogais existentes na lista', listaDeVogais)
