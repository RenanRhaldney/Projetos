contador = 0
maiorNumero = 0

print('Informe 5 numeros')

while contador < 5:
    contador += 1
    number = int(input(f'Numero {contador}: '))
    if maiorNumero < number:
        maiorNumero = number

print('O maior numero informado foi', maiorNumero, '.')
print('FIM...')