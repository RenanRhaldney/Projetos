number = int(input("Informe um numero. "))
contador1 = 0

for i in range(1, number + 1):
    restoDaDivisao = number % i
    if restoDaDivisao == 0:
        contador1 +=1

if contador1 > 2:
    print("NUMERO NAO É PRIMO")
else:
    print("NUMERO É PRIMO")

print("FIM...")