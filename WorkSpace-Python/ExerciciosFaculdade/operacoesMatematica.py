number1 = int(input("Digite um numero. "))
number2 = int(input("Digite outro numero."))

soma = int(number1 + number2)
subtracao = int(number1 - number2)
multiplicacao = int(number1 * number2)
divisao = int(number1 / number2)

print(" ")
print(type(soma))
print(type(subtracao))
print(type(multiplicacao))
print(type(divisao))

print(f"\nSoma = {soma}\n"
      f"Subtracao = {subtracao}\n"
      f"multiplicacao = {multiplicacao}\n"
      f"divisao = {divisao}\n")

converter = str(divisao)
print(type(converter))
