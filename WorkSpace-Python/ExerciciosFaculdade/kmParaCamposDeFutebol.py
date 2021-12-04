km = float(input("Informe quantos km são. "))
#convertendo km para km²
kmAoQuadrado = km ** 2
areaCamposDeFutebol = 75 * 110
#convertendo km² para m² e dividindo por m² de campos de futebol
quantidadeDeCampos = (kmAoQuadrado * 1000000) / areaCamposDeFutebol
#a funcao round, se nao colocar a quantidade de casas decimais, ele arredonda o valor para cima
print("quantidade de campos de futebol {}".format(round(quantidadeDeCampos)))