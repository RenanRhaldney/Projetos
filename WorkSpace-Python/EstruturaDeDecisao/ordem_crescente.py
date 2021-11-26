number1 = int(input("Digite 3 numeros.\n"))
number2 = int(input())
number3 = int(input())

if number1 < number2 and number1 < number3:
    print(number1)
    if number2 < number3:
        print(number2)
        print(number3)
    else:
        print(number3)
        print(number2)
elif number2 < number1 and number2 < number3:
    print(number2)
    if number1 < number3:
        print(number1)
        print(number3)
    else:
        print(number3)
        print(number1)
elif number3 < number1 and number3 < number2:
    print(number3)
    if number1 < number2:
        print(number1)
        print(number2)
    else:
        print(number2)
        print(number1)
print("FIMMMMMMMMMMMMMMM")