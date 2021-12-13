populacao1 = 8000
populacao2 = 20000
anos = 0
while populacao1 < populacao2:
    anos += 1
    populacao1 = populacao1 / 100 * 103
    populacao2 = populacao2 / 100 * 101.5

print(anos)