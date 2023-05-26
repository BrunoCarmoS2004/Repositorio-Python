import os
os.system('cls')  
carros=[]
carro=input("Digite um carro..: ")
while carro != "-1":
    carros.append(carro)
    carro=input("Digite um carro..: ")
os.system('cls')    
for iten in carros:
    print(iten)
    