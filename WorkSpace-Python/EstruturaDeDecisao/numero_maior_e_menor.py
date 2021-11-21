number1 = float(input("Informed three numbers.\n"))
number2 = float(input())
number3 = float(input())

if number1 > number2 and number1 > number3:
    print(f"Highest number informed is {number1:.2f}")
elif number2 > number1 and number2 > number3:
    print(f"Highest number informed is {number2:.2f}")
else:
    print(f"Highest number informed is {number3:.2f}")

if number1 < number2 and number1 < number3:
    print(f"Low number informed is {number1:.2f}")
elif number2 < number1 and number2 < number3:
    print(f"Low number informed is {number2:.2f}")
else:
    print(f"Low number informed is {number3:.2f}")