class Calculadora:

    # metodo __init__ é utilizado para receber os atributos do objeto
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    # o self se utiliza para acessar o valores que estão dentro da classe
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


# só vai se executado quando for chamado pelo proprio arquivo
if __name__ == '__main__':
    calculadora = Calculadora(1, 2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
