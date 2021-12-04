metros = float(input("Informe quantos metros são. "))

pes = 30.48
conversao = metros / (pes / 100)

print("{} metros da {} pes.".format(metros, round(conversao, 2)))