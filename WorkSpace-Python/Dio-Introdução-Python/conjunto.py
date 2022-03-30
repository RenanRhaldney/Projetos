conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 3, 9, 10, 7}

print(type(conjunto))

# variavel tipo conjunto não deixa ter elemento repetido
# unir 2 variaveis tipo conjunto
conjunto_uniao = conjunto.union(conjunto2)
print('Unindo 2 conjuntos {}'.format(conjunto_uniao))

# intersecção é verificar se existe nos conjuntos 2 valores iguais nos mesmos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Conjunto intersecção {}'.format(conjunto_interseccao))

# verifica os valores diferentes entre os conjuntos informados
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Verificando valores diferentes entre os conjuntos 1 e 2 {}'.format(conjunto_diferenca1))
print('Verificando valores diferentes entre os conjuntos 2 e 1 {}'.format(conjunto_diferenca2))

# exibe os numeros que não são iguais entre os conjuntos
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica {}'.format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'passaro']
conjunto_animais = set(lista)
print(conjunto_animais)

# para adicionar um item no conjunto
conjunto.add(6)
print('Adicionando valor 6 no conjunto {}'.format(conjunto))

#remover item do conjunto
conjunto.discard(3)
print('Removendo o valor 3 {}'.format(conjunto))

