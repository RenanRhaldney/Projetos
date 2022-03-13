# usando a função input no python, a variavel recebe um valor tipo string
# então como quero um valor numerico, converti o valor para int
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    print('O maior valor é {}'.format(valor1))

elif valor2 > valor1 and valor2 > valor3:
    print('O maior valor é {}'.format(valor2))

elif valor3 > valor1 and valor3 > valor2:
    print('O maior valor é {}'.format(valor3))

else:
    print('Numeros informados são iguais.')
