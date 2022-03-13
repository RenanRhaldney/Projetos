b1 = int(input('Primeiro bimestre: '))
b2 = int(input('Segundo bimestre: '))
b3 = int(input('Terceiro bimestre: '))
b4 = int(input('Quarto bimestre: '))
media = (b1+b2+b3+b4)/4

if media > 10:
    print('Alguma nota foi informada arrada.')
elif media >= 7:
    print('Parabens você foi aprovado, sua media ficou {}'.format(media))
else:
    print('Você reprovou, sua media ficou {} estude mais na proxima vez'.format(media))
