lista = []
soma = 0
multiplicacao = 1

print('Digite 5 numeros.')

for i in range(5):
    lista.append(int(input()))
    soma += lista[i]
    multiplicacao *= lista[i]


print(f'Lista {lista}\n'
      f'Soma da lista = {soma}\n'
      f'Multiplicacao da lista = {multiplicacao}')
