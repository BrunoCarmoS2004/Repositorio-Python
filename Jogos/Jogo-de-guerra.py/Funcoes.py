import os
import random
import time




os.system("cls")
class NPC: #Base/Pai
    def __init__(self, nome, vida, energia, municao, dano):
       self.nome=nome 
       self.vida=vida
       self.municao=municao
       self.energia=energia
       self.dano=dano
    def info(self):
        print("Nome....: " + self.nome)
        print("vida....: " +str(self.vida))  
        print("Energia.: " +str(self.energia))  
        print("Munição.: " +str(self.municao))  
        print("Dano.: " +str(self.dano))    
        print("---------------------------------------")
        
        
class Normalzinho(NPC):
    def __init__(self):
        self.nome="Normalzinho"
        self.vida=100 
        self.municao=55
        self.energia=100
        self.dano=5
        super().__init__(self.nome, self.vida, self.municao, self.energia, self.dano)   
        
         
class Rapidinho(NPC):
    def __init__(self):
        self.nome="Rapinho"
        self.vida=80 
        self.municao=60
        self.energia=150
        self.dano=3
        super().__init__(self.nome, self.vida, self.municao, self.energia, self.dano)


        
class Fortinho(NPC):
    def __init__(self):
        self.nome="Fortinho"
        self.vida=200 
        self.municao=80
        self.energia=50
        self.dano=10
        super().__init__(self.nome, self.vida, self.municao, self.energia, self.dano)
    
class Lojinha(NPC):
    def __init__(self):
        self.nome="Lojinha"
        self.vida=100 
        self.municao=55
        self.energia=100
        self.dano=5
        super().__init__(self.nome, self.vida, self.municao, self.energia, self.dano)
        
class Jogador(NPC):
   def __init__(self, nome, vida, energia):
      self.municao=50
      self.dano=5
      super().__init__(nome, vida, energia, self.municao, self.dano)
    
    
    
            
Norm=Normalzinho()
Rapi=Rapidinho()
Fort=Fortinho()
Loji=Lojinha()


def tabela():
   print("O que quer fazer agora?")
   print("""
1 - Ir a luta!
2 - Comprar munição e vida
3 - Descançar
4 - Comprar nova arma
5 - Desistir...
            """)
   
def Jogo_principal():
    global inimigo_vida
    rand=random.randrange(1,100)
    if (rand >=1 and rand <= 40):
       
        inimigo_nome = "Soldado"
        inimigo_vida = 100
        
        
        print("Você encontrou um soldado inimigo!")
        print("O que vai fazer agora?")
        
    elif (rand > 33 and rand <= 30):
        inimigo_vida = 80
        inimigo_nome = "Soldado rápido"
        print("Rapidinho")
        
    elif (rand > 66 and rand <= 20):
        inimigo_vida = 200
        inimigo_nome = "Soldado de elite"
        print("Fortinho")
        
    elif (rand > 90 and rand <=10):
        inimigo_vida = 100
        inimigo_nome = "Mercador"
        print("Lojinha")
    
def Tabela_batalha():
    #ARRUMAR ISSOOOOOOOOOOOOOOO
    inimigo_vida
    while (inimigo_vida > 0 or esc_bat_tab != 2):
        print("--------------------------------------------------------------")
        print("|1 - ATACAR | 2 - RECUAR | 3 - DEFENDER | 4 - RECUPERAR VIDA |")   
        print("--------------------------------------------------------------")
        esc_bat_tab = input("Sua escolha: ")
        if (esc_bat_tab == 1):
            rand=random.randrange(1,100)
            if (rand <= 60):
                print("Você acertou ele!")
                print("O "+inimigo_nome+ "esta com "+inimigo_vida+" de vida!")
        elif (esc_bat_tab == 3):
            if (Jogador.energia >= 100):
                print("Batata")
            
        
    
#Norm.info()
#Rapi.info()
#Fort.info()
#Joga.info()
#Loji.info()
