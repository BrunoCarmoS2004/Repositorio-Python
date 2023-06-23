import os
import time
from Funcoes import *
import random
resultado = 1

Jogo_principal()
print("Bem vindo ao Campo de batalha...")
print()

esc1=input("Escolha a nome do seu Soldado..:")
print()


while resultado == 1:
   os.system('cls')
   print("ATENÇÃO!! Agora você ira escolher o a vida do seu personagem e depois a energia")
   print("Sua vida e energia precisam estar em equilibrio")
   print()
   print("Exemplo:")
   print()
   print("1  =< Vida <= 50   --> energia <> 50 --> MAX = 150")
   print("50 =< Vida <= 75   --> energia <> 50 --> MAX = 120")
   print("75 =< Vida <= 100  --> energia <> 50 --> MAX =  80")
   print("100 =< Vida <= 150  --> energia <> 50 --> MAX = 50")
   print()
   print()


   esc2=int (input("Escolha a vida do seu personagem..:"))
   print()
   esc3=int (input("Escolha a energia do seu personagem..:"))
   print()
   #VIDA 1
   if (esc2 >= 1) or (esc3 <= 50):
      if (esc3 >=1 and esc3 <= 150):
         print("Personagem PERFEITO!!")
         resultado = 2
         os.system('pause')
      else:
         print("Personagem em desequilibrio, revise a tabela e tente novamente")
         print()
         os.system('pause')
   #VIDA 2
   elif (esc2 >= 50) or (esc3 <= 75):
      if (esc3 >=1 and esc3 <= 120):
         print("Personagem PERFEITO!!")
         resultado = 2
         os.system('pause')
      else:
         print("Personagem em desequilibrio, revise a tabela e tente novamente")
         print()
         os.system('pause')
         
   #VIDA 2
   elif (esc2 >= 75) or (esc3 <= 100):
      if (esc3 >=1 and esc3 <= 80):
         print("Personagem PERFEITO!!")
         resultado = 2
         os.system('pause')
      else:
         print("Personagem em desequilibrio, revise a tabela e tente novamente")
         print()
         os.system('pause')
         
   #VIDA 2
   elif (esc2 >= 100) or (esc3 <= 150):
      if (esc3 >=1 and esc3 <= 50):
         print("Personagem PERFEITO!!")
         resultado = 2
         os.system('pause')
      else:
         print("Personagem em desequilibrio, revise a tabela e tente novamente")
         print()
         os.system('pause')
os.system('cls')   
print("Olá "+esc1+"! Olhe ao seu redor! esse local será seu desfecho final!")
print()
print("Nesse jogo você tera que batalhar contra 3 inimigos sem morrer para nenhum deles")
print()
print("Aqui estão suas informações: ")
print()
Joga=Jogador(esc1, esc2, esc3)
Joga.info()      
print()
print("Essas informações poderam ser mudadas com o tempo!")  
print()
print("Bora dar o proximo passo!") 
print()
os.system('pause')
os.system('cls')
tabela()
tab_esco = input("Escolha uma das opções acima..:")
"""
print("1 - Próximo inimigo")
   print("2 - Comprar munição e vida")
   print("2 - Descançar")
   print("3 - Comprar nova arma")
   
"""






   