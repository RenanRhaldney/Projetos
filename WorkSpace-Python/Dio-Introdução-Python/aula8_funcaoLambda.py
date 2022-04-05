# a função lambda é uma funçã oculta ou seja a variavel que a receber "se torna uma função"
contador_letrar = lambda lista: [len(x) for x in lista]

listaDeAnimais = ['gato', 'cachorro', 'tartaruga']
print(contador_letrar(listaDeAnimais))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a + b,
    'multiplicacao': lambda a, b: a + b,
    'divisao': lambda a, b: a + b,
}
somar = calculadora['soma']
print(somar(1, 2))

mult = calculadora['multiplicacao']
print(mult(3, 3))
