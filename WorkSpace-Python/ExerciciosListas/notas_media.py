nota = []
print('Adicione as notas no sistema.')
#adicionando dados na lista
for i in range(1, 5):
    nota.append(float(input(f'Nota {i}: ')))

#Exibir notas e calcular media das notas
print('Notas:', nota, '\nMedia =', (nota[0] + nota[1] + nota[2] + nota[3]) / len(nota))