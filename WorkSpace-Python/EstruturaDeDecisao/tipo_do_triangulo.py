lado1 = int(input('Informe a medida dos 3 lados do triangulo.\nL1: '))
lado2 = int(input('L2: '))
lado3 = int(input('L3: '))

if lado1 == lado2 and lado2 == lado3:
    print('Triangulo Equilatero.')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triagulo Esacaleno.')
else:
    print('Triagulo Isosceles.')

print('FIM...')