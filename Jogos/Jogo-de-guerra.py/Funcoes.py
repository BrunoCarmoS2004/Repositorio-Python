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
loji=Lojinha()

def tabela():
   print("O que quer fazer agora?")
   print("""
1 - Próximo inimigo
2 - Comprar munição e vida
3 - Descançar
4 - Comprar nova arma
            """)
   
def Jogo_principal():
    rand=random.randrange(1,100)
    if (rand >=1 and rand <= 33):
        print("Normalzinho")
        
    elif (rand > 33 and rand <= 66):
        print("Rapidinho")
        
    elif (rand > 66 and rand <= 90):
        print("Fortinho")
        
    elif (rand > 90 and rand <=100):
        print("Lojinha")
    

   

#Norm.info()
#Rapi.info()
#Fort.info()
#Joga.info()
