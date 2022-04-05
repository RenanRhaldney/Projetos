class Calculadora:

    # o __init__ não pode ficar vazio, se não da erro, se utiliza o pass para quando entrar no metodo passar para o proximo metodo
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


# só vai se executado quando for chamado pelo proprio arquivo
if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(5, 5))
    print(calculadora.subtracao(5, 5))
    print(calculadora.multiplicacao(2, 5))
    print(calculadora.divisao(25, 5))

