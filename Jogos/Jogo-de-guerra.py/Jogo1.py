import os
import time
from Funcoes import *
import random
resultado = 1


print("Bem vindo ao Campo de batalha...")
print()

esc1=input("Escolha a nome do seu Soldado..:")
print()


while resultado == 1:
   os.system('cls')
   print("ATENÇÃO!! Agora você ira escolher o a vida do seu personagem e depois a energia")
   print("")
   print("Você tem 200 pontos para gastar em vida e energia, escolha sabiamente...")
   print("")
   os.system('pause')
   print("")
   os.system('cls')
   esc2=int (input("Escolha a vida do seu personagem..:"))
   print()
   sobra = str(200 - esc2)
   print("Sobrou "+sobra+" pontos para serem usados na energia")
   print()
   esc3=int (input("Escolha a energia do seu personagem..:"))
   print()
   #VIDA 1
   if (esc2 + esc3 <= 200):
      print("Personagem PERFEITO!!")
      print()
      resultado = 2
      os.system('pause')
   else:
      print("Personagem muito poderoso tente novamente...")
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
Tabela_batalha()







   