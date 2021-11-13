# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

height = float(input("Inform your height to know weight your ideal.\n"))

men = 72.7 * height - 58
woman = 62.1 * height - 44.7

print("Weight ideal to men {}Kg".format(round(men, 2)))

print("Weight ideal to woman {}Kg".format(round(woman, 2)))