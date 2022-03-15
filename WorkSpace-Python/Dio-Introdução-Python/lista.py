#lista sempre vai ser dentro de cochetes
#podendo ser lista de inteiros, lista de ponto fluante, lista de string ou lista mista
lista = [1, 3, 88, 16, 33]
lista_animal = ['cachorro', 'gato', 'passarinho']
#pode mutiplicar a lista (repetir)
nova_lista = lista_animal * 3

print(nova_lista)

if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

#função para adicionar item na lista
lista_animal.append('peixe')

#retira a ultima posição da lista por padrão se nao passar parametro
lista_animal.pop(2)

#remove o item de lista de acordo com o parametro passado
lista_animal.remove('cachorro')

#Ordena a lista
lista_animal.sort()
lista.sort()

#ordena de um modo invertido
lista_animal.reverse()

#função SUM(nomeDaLista) ja soma todos os numeros dentro da lista
print(sum(lista))

#função MAX(nomeDaLista) retorna o maior numero dentro da lista]
print(max(lista))

#função MIN(nomeDaLista) retorna o menor numero dentro da lista
print(min(lista))

#se for utilizar essa função numa lista de strings, ela retorna a string que iniciar
#com mais proxima do final de acordo com a ordem alfabetica
print(max(lista_animal))

#se for utilizar essa função numa lista de strings, ela retorna a string que iniciar
#com mais proxima do inicio de acordo com a ordem alfabetica
print(min(lista_animal))


