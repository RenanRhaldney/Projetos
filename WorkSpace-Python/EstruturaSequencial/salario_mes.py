# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

value_hour = float(input("Informed how many you win by hour.\n"))
hour_works = float(input("how many hour you worked this month?\n"))
gross_salary = value_hour * hour_works
discount_ir = 11 / 100 * gross_salary
discount_inss = 8 / 100 * gross_salary
discount_synd = 5 / 100 * gross_salary
total_discounts = discount_ir + discount_inss + discount_synd
net_salary = gross_salary - total_discounts

#print("Gross salary = R${}\n"
#      "Discount IR = R${}\n"
#      "Discount INSS = R${}\n"
#      "Discount Syndicate = R${}\n"
#      "Net salary = R${}".format(gross_salary, discount_ir, discount_inss, discount_synd, net_salary))


print(f"Gross salary = R${gross_salary:.2f}\n"
      f"Discount IR = R${discount_ir:.2f}\n"
      f"Discount INSS = R${discount_inss:.2f}\n"
      f"Discount Syndicate = R${discount_synd:.2f}\n"
      f"Net salary = R${net_salary:.2f}")