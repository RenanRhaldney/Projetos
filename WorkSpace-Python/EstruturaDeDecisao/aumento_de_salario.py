salary = float(input("Infomed your salary. "))

if salary < 280:
    percentage = 20
    salaryWithCurrent = salary * (percentage + 100) / 100
    print(f"Salary previous R${salary:.2f}\n"
          f"readjustment of {percentage:.0f}%\n"
          f"increase of R${salaryWithCurrent - salary:.2f}\n"
          f"Salary current R${salaryWithCurrent:.2f}")

elif salary >= 280 and salary < 700:
    percentage = 15
    salaryWithCurrent = (percentage + 100) * salary / 100
    print(f"Salary previous R${salary:.2f}\n"
          f"readjustment of {percentage:.0f}%\n"
          f"increase of R${salaryWithCurrent - salary:.2f}\n"
          f"Salary current R${salaryWithCurrent:.2f}")

elif salary >= 700 and salary < 1500:
    percentage = 10
    salaryWithCurrent = (percentage + 100) * salary / 100
    print(f"Salary previous R${salary:.2f}\n"
          f"readjustment of {percentage:.0f}%\n"
          f"increase of R${salaryWithCurrent - salary:.2f}\n"
          f"Salary current R${salaryWithCurrent:.2f}")

else:
    percentage = 5
    salaryWithCurrent = (percentage + 100) * salary / 100
    print(f"Salary previous R${salary:.2f}\n"
          f"readjustment of {percentage:.0f}%\n"
          f"increase of R${salaryWithCurrent - salary:.2f}\n"
          f"Salary current R${salaryWithCurrent:.2f}")

print('The end')