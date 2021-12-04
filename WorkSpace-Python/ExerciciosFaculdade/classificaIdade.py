idade = int(input("Informed your age. "))

if idade >= 1 and idade < 12:
    print("CRIANCA")
elif idade >= 12 and idade < 18:
    print("ADOLESCENTE ")
elif idade >= 18 and idade < 32:
    print("JOVEM")
elif idade >= 32 and idade < 60:
    print("ADULTO")
elif idade >= 60 and idade <= 120:
    print("IDOSO")
else:
    print("IDADE INVALIDA")