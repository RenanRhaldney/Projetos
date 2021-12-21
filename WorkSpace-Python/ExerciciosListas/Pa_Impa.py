listaPrincipal = []
pa = []
impa = []

print('Informe 10 numeros. ')
for i in range(10):
    listaPrincipal.append(int(input()))
    if listaPrincipal[i] % 2 == 0:
        pa.append(listaPrincipal[i])
    else:
        impa.append(listaPrincipal[i])

print(f'LISTA PRINCIPAL = {listaPrincipal}\n'
      f'PA = {pa}\n'
      f'IMPA = {impa}')