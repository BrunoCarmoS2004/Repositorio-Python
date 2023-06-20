import os

carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self, nome, pot):
        self.nome=nome
        self.pot=pot
        self.velMax=int(pot)*2
        self.ligado=False
        
    def ligar(self):
        self.ligado=True
        
    def desligar(self):
        self.ligado=False
        
    def info(self):
        print("Nome..:"+self.nome)
        print("Potencia..:"+str(self.pot))
        print("Vel Maxima..:"+str(self.velMax))
        print("Ligado?..:"+("Sim" if self.ligado == True else "Não"))
    
def Menu():
        os.system('cls') or None
        print("1 - Novo Carro")
        print("2 - Informações do novo Carro")
        print("3 - Excluir Carro")
        print("4 - Ligar ou Desligar Carro")
        print("5 - Listar Carros")
        print("6 - Sair")
        print("Quantidade de carros..:"+str(len(carros)))
        opc=int(input("Digite uma opção..:"))
        return opc
      

def NovoCarro():
    os.system('cls') or None
    n=input("Digite o nome do carro..:")
    p=input("Digite a potencia do carro..:")
    car=Carro(n,p)
    carros.append(car)
    print("Carro criado com sucesso")
    print("Precione uma tecla")
    os.system("pause")
    
def Informacoes():
    os.system('cls') or None
    n=input("Informe o numero do Carro que deseja ver as informações..:")
    try:
        carros[int(n)].info()
    except:
        print("Carro não existe na lista")
    print("Precione uma tecla")
    os.system("pause")
    
def ExcluirCarro():
    os.system('cls') or None
    n=input("Informe o numero do Carro que deseja excluir..:")
    try:
        del carros[int(n)]
    except:
        print("Carro não existe na lista")
    print("Precione uma tecla")
    os.system("pause")
    
def LigarDesligar():
    os.system('cls') or None
    n=input("Informe o numero do Carro que deseja Ligar ou Desligar..:")
    try:
            resp=input("Digite 1 para LIGAR e 2 para DESLIGAR..:")
            if resp == "1":
                    carros[int(n)].ligar()
            elif resp == "2":
                    carros[int(n)].desligar()
            else:
                    print("Opção invalida")
    except:
        print("Carro não existe na lista")
    print("Precione uma tecla")
    os.system("pause")
    
def listarCarros():
    os.system('cls')
    p=0
    for c in carros:
        print(str(p) +" - " +c.nome)
        p=p+1
    print("Precione uma tecla")
    os.system("pause")
    
ret=Menu()
while ret < 6:
    if ret == 1:
        NovoCarro()
        ret = 0
    elif ret== 2:
        Informacoes()
        ret = 0
    elif ret==3:
        ExcluirCarro()
        ret = 0
    elif ret==4:
        LigarDesligar()
        ret = 0
    elif ret==5:
        listarCarros()
        ret = 0
    elif ret==0:
        ret=Menu()
ret=Menu()
        
os.system('cls') or None
print("Programa Finalizado")
