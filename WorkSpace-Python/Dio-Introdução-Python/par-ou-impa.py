number1 = int(input('informe um numero '))
# % resulta no resto da divisão que vai ser 0 ou 1
resto = number1 % 2

if resto == 0:
    print(number1, 'é par')
else:
    print(number1, 'é impa')
