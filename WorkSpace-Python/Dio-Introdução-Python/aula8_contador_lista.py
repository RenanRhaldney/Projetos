def contarItensLista(lista):
    contador = []
    for i in lista:
        quantidade = len(i)
        contador.append(quantidade)
    return contador


if __name__ == '__main__':
    lista = ['renan', 'rhaldney']
    print(contarItensLista(lista))
