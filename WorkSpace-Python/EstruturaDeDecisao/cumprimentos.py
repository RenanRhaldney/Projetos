cumprimento = input("Qual o turno que você estuda, matutino, vespertino ou nortuno?\n")

#A funcao cumprimento() faz com que a primeira letra da string seja maiuscula.
cumprimento = cumprimento.capitalize()

if cumprimento[0] == 'M':
    print("Bom dia.")
elif cumprimento[0] == 'V':
    print("Boa Tarde.")
elif cumprimento[0] =='N':
    print("Boa noite.")
else:
    print("Turno invalido.")

