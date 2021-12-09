number = int(input("Digite um numero para saber o fatorial do mesmo. "))
fatorial = number

for i  in range(1, number):
    fatorial *= i

print(f"Fatorial de {number} = {fatorial}.")

print("FIM...")