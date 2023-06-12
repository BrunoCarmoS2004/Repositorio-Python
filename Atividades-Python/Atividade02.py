print("Bem vindo ao Criador de Carros!")



vm=input("Primeiro...Defina a velociadade máxima do carro..:")
cr=input("Segundo...Defina a cor do carro..:")
li=input("Terceiro...Defina se o carro esta ligado ou não")

class carro:
    velMax=0
    cor=""
    estado=False
    def __init__(self):
        self.velMax=vm
        self.cor=cr
        self.estado=li
    def mostrar(self):
        print("--------------------------------------")
        print("Velociadade Maxima: "+ str(self.valMax))
        print("Cor...............: "+ str(self.cor))
        print("Ligado?...........: "+ str(self.ligado))
        print("--------------------------------------")
print(carro)