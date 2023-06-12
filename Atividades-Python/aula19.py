class Carro:
    valMax=0
    ligado=False
    cor=""

c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.valMax=200
c1.cor="Preto"
if (Carro.ligado == False):
    c1.ligado="Não"
else:
    c1.ligado="Sim"
    


print("Velociadade Maxima: "+ str(c1.valMax))
print("Cor: "+ str(c1.cor))
print("Ligado?: "+ str(c1.ligado))

