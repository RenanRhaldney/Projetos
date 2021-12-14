soma = 0
media = 0

print('Informe 5 numeros.')

for i in range(1,6):
    number = int(input(f'Numero {i}: '))
    soma += number
    media = soma / i
    print(f'SOMA = {soma}.')
    print(f'MEDIA = {media:.2f}.')

print('FIM...')