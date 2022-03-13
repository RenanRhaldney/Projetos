a = 23
b = 15
frase = 'eu sou uma string'
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print('utilizando a função .format().\n'
      'soma = {}\nsubtração = {}\nmultiplicação = {}\ndivisão = {}\nfrase = {}'
      .format(soma, subtracao, multiplicacao, divisao, frase))

print('--------------------------------------//------------------------------------')

print('outra forma de usar a função .format().\n'
      'soma = {soma}\nsubtração = {sub}\nmultiplicação = {mult}\ndivisão = {div}\nfrase = {frase}'
      .format(sub=subtracao, frase=frase, div=divisao, mult=multiplicacao, soma=soma))
