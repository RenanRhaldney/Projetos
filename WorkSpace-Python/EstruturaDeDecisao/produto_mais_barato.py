#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.
print("Informe o preco dos produtos a seguir.")
precoProduto1 = float(input("Camisa: "))
precoProduto2 = float(input("Calca: "))
precoProduto3 = float(input("Sapato: "))

if precoProduto1 < precoProduto2:
    if precoProduto1 < precoProduto3:
        print("Compre a camisa!")
    else:
        print("Compre o Sapato!")
elif precoProduto2 < precoProduto3:
    print("Compre a Calca!")
else:
    print("Compre o sapato!")

print("FIM DO PROGRAMA")