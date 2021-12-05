number = int(input("Digite um numero para saber o somatorio ate ele. "))
somatorio = 0

for contador in range(number + 1):
    somatorio = somatorio + contador

print("\nResultado do somatorio de 1 ate {} e {}.".format(number, somatorio))
print("FIM...")