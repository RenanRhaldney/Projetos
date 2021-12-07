print("Forneca os dados solicitados abaixo.")
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salario: "))
sexo = str.capitalize(input("Sexo: "))
estadoCivil = str.capitalize(input("Estado civil: "))


if len(nome) <= 3:
    print("O nome precisa ser maior que 3 characteres. ")
elif idade <= 0 or idade > 150:
    print("Idade invalida.")
elif salario <= 0:
    print("Salario invalido.")
elif sexo[0] != "F" and sexo[0] != "M":
    print("Sexo invalido.")
elif estadoCivil[0] != "S" and estadoCivil[0] != "C" and estadoCivil[0] != "V" and estadoCivil[0] != "D":
    print("Estado civil invalido.")
else:
    print("\nCadastro realizado com sucesso.\n")

print("FIM...")