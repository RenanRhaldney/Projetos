class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 11

    # Um metodo não tem retorno
    def power(self):
        # Não precisa verificar se é True ou False numa variável tipo Boolean
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminuir_canal(self):
        if self.ligada:
            self.canal -= 1


televisao = Televisao()

# True / canal + 1
televisao.power()
televisao.aumenta_canal()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('aumentando canal: {}\n'.format(televisao.canal))

# False / canal - 1
televisao.power()
televisao.diminuir_canal()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('diminuindo canal: {}\n'.format(televisao.canal))
# True / canal + 1
televisao.power()
televisao.aumenta_canal()
print('Televisão está ligada: {}'.format(televisao.ligada))
print('aumentando canal: {}'.format(televisao.canal))
