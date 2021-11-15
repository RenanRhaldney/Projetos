# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Informed in fahrenheit for to discover how much of in celsius.\n"))
celsius = 5 * ((fahrenheit-32)/9)
print("{} Celsius".format(round(celsius, 2)))