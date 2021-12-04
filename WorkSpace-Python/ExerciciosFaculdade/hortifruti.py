maca = float(input("Informe quantas macas voce deseja comprar. "))

if maca < 15 and maca > 0:
    valorDaCompra = 0.3 * maca
    print("Total a pagar e R${}".format(round(valorDaCompra, 2)))
elif maca >= 15:
    valorDaCompra = 0.25 * maca
    print("Total a pagar e R${}".format(round(valorDaCompra, 2)))
else:
    print("Quantidade invalida.")

print("FIM...")