#range(inicia, ate, de quanto em quanto)
#for indice in range(1, 100, 3):
#    print(x)

number = int(input('Informe um numero: '))

for i in range(1, number):
    if i % 2 == 0:
        print(i)

#vai repetir ate uma condição ser satisfeita
while number < 10:
    print(number)
    number +=1
