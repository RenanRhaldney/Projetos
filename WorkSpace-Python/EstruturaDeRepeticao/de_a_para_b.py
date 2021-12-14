number1 = int(input('Informe dois numero.\n'))
number2 = int(input())
soma = 0
#programa informa a soma entre os numeros informados
if number1 < number2:
    for i in range(number1 + 1, number2):
        soma += i
        print(soma)
else:
    for i in range(number2 + 1, number1):
        soma += i

print(f'Resultado da soma {soma}')
print('FIM...')