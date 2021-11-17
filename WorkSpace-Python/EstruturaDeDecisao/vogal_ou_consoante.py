letra = input("type it a letter.\n")

#Função .isalpha retorna true se tiver algum caracter na string tipo numero
if letra.isalpha():
    if letra == 'a' or letra == 'A':
        print("Vogal")
    elif letra == 'e' or letra == 'E':
        print("Vogal")
    elif letra == 'i' or letra == 'I':
        print("Vogal")
    elif letra == 'o' or letra == 'O':
        print("Vogal")
    elif letra == 'u' or letra == 'U':
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Character informed not is a letter")

