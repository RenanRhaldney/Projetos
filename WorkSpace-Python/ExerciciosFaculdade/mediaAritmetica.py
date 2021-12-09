number = []
interromper = "s"
print("Informe os numeros para saber a media aritmetica deles.")
while interromper == "s":
    number.append(int(input()))
    number.append(int(input()))
    number.append(int(input()))
    number.append(int(input()))

    interromper = input("Deseja continuar?\n")

print("media aritmetica = ", sum(number) / len(number))


