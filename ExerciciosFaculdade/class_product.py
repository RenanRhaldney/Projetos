class Produto:
    def __init__(self, nome, preco, cor, garantia):
        self.nome = nome
        self.preco = preco
        self.garantia = garantia
        self.cor = cor


    def atualizar_preco(self, novo_preco):
        
        print("Preço atualizado.")

    def desconto(self, desconto):
        self.preco -= desconto
        print("Preço com desconto é R${}".format(round(self.preco, 2)))

    def mudar_cor(self,cor):
        self.cor == cor
        print("A Cor escolhida foi {} ".format(self.cor))
    def descricao(self):
        print("Produto {}, cor {}, preço R${}, 1 ano de garantia.".format(self.nome, self.cor, self.preco))

    def validacao_garantia(self, garantia):
        if garantia:
            print("A {} ainda está na garantia.".format(self.nome))
            self.garantia = garantia
        else:
            print("A garantia da {} expirou.".format(self.nome))
            self.garantia = garantia