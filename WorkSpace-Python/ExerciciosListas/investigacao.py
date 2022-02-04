perguntas = ['1-Telefonou para a vitima?', '2-Esteve no local do crime?', '3-Mora perto da vitima?',
             '4-Devia para a vitima?', '5-Ja trabalhou com a vitima?']
nivelDeClassificacao = 0

#Fazer as Perguntas e verificar resposta
for i in perguntas:
    print(i)
    resposta = input().upper()
    if resposta[0] == 'S':
        nivelDeClassificacao += 1

#Verificar qual categoria
if nivelDeClassificacao == 2:
    print('Suspeita.')
elif nivelDeClassificacao == 3 or nivelDeClassificacao == 4:
    print('Cumplice.')
elif nivelDeClassificacao == 5:
    print('Assassino.')
else:
    print('Inocente.')
