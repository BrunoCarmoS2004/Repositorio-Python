from distutils.log import info
from turtle import st


class NPC: #Base/Pai
    def __init__(self, nome, time, forca, municao):
       self.nome=nome 
       self.time=time
       self.forca=forca
       self.municao=municao
       self.vivo= True
       self.energia= 100
    def info(self):
        print("Nome....: " + self.nome)
        print("Time....: " +str(self.time))  
        print("Força...: " +str(self.forca))   
        print("Minição.: " +str(self.municao))   
        print("Vivo?...: " +str(("sim" if self.vivo else "não")))    
        print("Energia.: " +str(self.energia))    
        print("---------------------------------------")
    
class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        super().__init__(nome, time, self.forca, self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=100
        self.municao=200
        super().__init__(nome, time, self.forca, self.municao)
        
class Elite(NPC):
    def __init__ (self, nome, time):
        self.forca=400
        self.municao=500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()
            
s1=Guarda("Popai desnutrido",1)
s2=Soldado("Atropelo da fimóse",1)
s3=Elite("Gatuno do meio dia",1)


s4=Guarda("Águia sem olhos",2)
s5=Soldado("Afonso pesca moça",2)
s6=Elite("Papaléguas sem perna",2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()