a = 23
b = 15
frase = 'eu sou uma string'
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print('tipos das variaveis iniciadas no escopo global.\n',
      'soma = ', type(soma), '\n'
      'subtração = ', type(subtracao), '\n'
      'multiplicação = ', type(multiplicacao), '\n'
      'divisão = ', type(divisao), '\n'
      'frase = ', type(frase))

print('----------------------//-------------------------- \n'
      'se converter o tipo da variavel dentro de algum comando, ela só vai ser convertida dentro desse comando\n'
      'e no escopo global vai permanecer o tipo da variavel original da entrada recebida inicialmente')
print(type(str(soma)))
print(type(soma))

print('----------------------//--------------------------\n'
      'dessa forma o tipo da variavel é convertida no escopo global')
soma = str(soma)
print(type(soma))

print('----------------------//--------------------------\n'
      'tambem podemos converter o resultado de um calculo')
divisao = str((b / a))
print(type(divisao))

