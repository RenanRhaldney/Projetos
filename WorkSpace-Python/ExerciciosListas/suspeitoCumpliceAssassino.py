perguntas = ['1-Telefonou para a vitima?', '2-Esteve no local do crime?', '3-Mora perto da vitima?',
             '4-Devia para a vitima?', '5-Ja trabalhou com a vitima?']
nivelDeClassificacao = 0

print('As perguntas feitas a seguir, devem ser respondidas com SIM ou NÃO.')

for i in perguntas:
    print(i)
    resposta = input().upper()
    if resposta[0] == 'S':
        nivelDeClassificacao += 1
        print('NIVEL DE CLASSIFICAÇÃO =', nivelDeClassificacao)

if nivelDeClassificacao == 0:
    print('INOCENTE!')
elif nivelDeClassificacao == 2:
    print('Suspeito!')
elif nivelDeClassificacao == 3 or nivelDeClassificacao == 4:
    print('Cumplice!')
else:
    print("ASSASSINO!")

