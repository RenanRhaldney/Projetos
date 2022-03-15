a = int(input('Entre com um valor: '))
#vai repetir ate o valor informado
for number in range(a):
    #vai contar a quantidade de numeros que é dividivo por (number)
    contador = 0
    #for para verificar e contar quantos numero resultam em 0 ate o valor de number
    for i in range(1, number+1):
        resto = number % i
        if resto == 0:
            contador += 1
    if contador == 2:
        print(number)

