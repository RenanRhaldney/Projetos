numeroAnterior = 0
numeroAtual = 1

print(f'{numeroAnterior}\n{numeroAtual}')

while numeroAtual < 500:

    fibonaci = numeroAnterior + numeroAtual
    numeroAnterior = numeroAtual
    numeroAtual = fibonaci
    print(fibonaci)

print('FIM...')