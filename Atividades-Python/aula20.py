from operator import truediv
from unittest.mock import seal


class Carro:
    valMax=0
    ligado=False
    cor=""
    def __init__(self,vm,li,cr):
        self.valMax=vm
        self.cor=cr
        self.ligado=li
    def mostrar (self):
        print("Velociadade Maxima: "+ str(self.valMax))
        print("Cor...............: "+ str(self.cor))
        print("Ligado?...........: "+ str(self.ligado))
        print("--------------------------------------")
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def andar(self):
        if(senf.ligado):
            print("Andando")
        else:
            print("Carro desligado")

c1 = Carro(200,False,"Preto")
c2 = Carro(120, False, "Branco")
c3 = Carro(350, False,"Vermelhor")


c1.desliga()
c1.mostrar()
c2.mostrar()
c3.mostrar()




