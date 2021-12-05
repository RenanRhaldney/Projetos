number = 0
contadorPa = 0
contadorImpa = 0

print("Digite 10 numeros. ")

for i in range(0, 10, 1):
    number = int(input())
    if number % 2 == 0:
        contadorPa += 1
    else:
        contadorImpa += 1

print(f"Quantidade de numeros PA {contadorPa}.\n"
      f"Quantidade de numeros IMPA {contadorImpa}.\n")

print("FIM...")