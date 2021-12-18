base = int(input('Qual a base da potencia? '))
expoente = int(input('Agora informe o expoente. '))
potencia = base

for i in range(1, expoente):
    potencia *= base

print(potencia)
print('FIM...')