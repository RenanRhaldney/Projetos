from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_lista import contarItensLista

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calculadora = Calculadora(1, 2)
print(calculadora.soma())
print(calculadora.multiplicacao())

# utilizando a função importada
lista = ['cachorro', 'gato', 'elefante']
print(contarItensLista(lista))

