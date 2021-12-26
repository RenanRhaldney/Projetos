listaPrincipal = []
continuar = 'S'

print('Informe o nome, idade e altura para cadastro.')

while continuar == 'S':
    pessoa = []

    #inserir dados
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Idade: ')))
    pessoa.append(float(input('Altura: ')))

    #adiciona uma lista dentro de outra lista
    listaPrincipal.append(pessoa)
    continuar = input('Desenha continuar aperte "S". ').upper()

#mostrar dados de cada pessoa
for i in range(len(listaPrincipal)):
    print(listaPrincipal[i])

#outro meio de exibir uma lista
#print(listaPrincipal[0], listaPrincipal[:0:-1])

