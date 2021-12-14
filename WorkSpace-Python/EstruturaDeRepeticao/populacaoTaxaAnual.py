populacao1 = int(input('Populacao do pais A. '))
populacao2 = int(input('Populacao do pais B. '))
anos = 0
#programa informa em quantos anos a populacao1 vai ultrapassar a populacao2
while populacao1 < populacao2:
    anos += 1
    populacao1 = populacao1 / 100 * 103
    populacao2 = populacao2 / 100 * 101.5

print(anos)