valorHora = float(input("Informe quanto voce ganha por hora. "))
horasTrabalhadas = float(input("Quantas horas você trabalhou esse mes? "))

salarioBruto = valorHora * horasTrabalhadas
impostoDeRenda = 0
inss = salarioBruto / 100 * 10
sindicato = salarioBruto / 100 * 3
fgts = salarioBruto / 100 * 11

if salarioBruto <= 900:
    print("Isento.")

elif salarioBruto > 900 and salarioBruto <= 1500:
    impostoDeRenda = salarioBruto / 100 * 5

elif salarioBruto > 1500 and salarioBruto <= 2500:
    impostoDeRenda = salarioBruto / 100 * 10

else:
    impostoDeRenda = salarioBruto / 100 * 20

salarioLiquido = salarioBruto - (impostoDeRenda + inss)

print(f"\nSalario Bruto R${salarioBruto:.2f}\n"
      f"Desconto de IR R${impostoDeRenda:.2f}\n"
      f"Desconto de INSS R${inss:.2f}\n"
      f"FGTS R${fgts:.2f}\n"
      f"Total de descontos R${impostoDeRenda + inss:.2f}\n"
      f"Salario Liquido R${salarioLiquido:.2f}")