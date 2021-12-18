#programa conta quantidade de numeros impa e pa informados
pa = 0
impa = 0

print('Informe 10 numeros. ')

for i in range(1, 11):
    number1 = int(input(f'{i} numero: '))
    if number1 % 2 == 0:
        pa += 1
    else:
        impa += 1

print(f'Quantidade de numeros PA informado foi {pa}.\nQuantidade de numeros IMPA informado foi {impa}')
print('FIM...')