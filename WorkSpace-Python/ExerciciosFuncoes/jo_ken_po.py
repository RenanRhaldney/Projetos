from random import randint as rd
from time import sleep
opcoes = ['PEDRA', 'PAPEL', 'TISOURA']
print("Escolha uma das opcoes abaixo para jogar.\n"
      "(1) Pedra\n"
      "(2) Papel\n"
      "(3) Tisoura")
computador = rd(0,2)
jogador = int((input("Qual é sua escolha? ")))
jogador -= 1
if jogador > 2:
      print("OPCAO INVALIDA")
else:
      sleep(0.6)
      print("JO")
      sleep(0.6)
      print("KEN")
      sleep(0.6)
      print("PO")
      sleep(0.6)
      print("-=" * 10)
      print(f"O computador jogou {opcoes[computador]}.\n"
            f"E voce escolheu {opcoes[jogador]}.")
      print("-=" * 10)

      if computador == 0:
            if jogador == 0:
                  print("EMPATE")
            elif jogador == 1:
                  print("VOCE GANHOU")
            elif jogador == 2:
                  print("COMPUTADOR GANHOU")
      elif computador == 1:
            if jogador == 0:
                  print("COMPUTADOR GANHOU")
            elif jogador == 1:
                  print("EMPATE")
            else:
                  print("VOCE GANHOU")
      elif computador == 2:
            if jogador == 0:
                  print("VOCE GANHOU")
            elif jogador == 1:
                  print("COMPUTADOR GANHOU")
            else:
                  print("EMPATE")
