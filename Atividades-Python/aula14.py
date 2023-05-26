import os
os.system('cls')

carro={"Fabricante":"Honda",
       "Modelo":"HVR",
       "Ano":"2016",
       "Cor":"Prata"
       }

print(carro["Modelo"])
print(carro["Fabricante"])
print(carro["Ano"])
print(carro["Cor"])
print("")
print(carro)
print("")
print("")


for x in carro:
    print(x)
    print(carro[x])
    
print("")
print("")
print("")
for x, c in carro.items():
    print(c+": "+ x)
    
print("")
if "Modelo" in carro:
    print("Sim")
    
print("Tamanho do Disctionary: "+str(len(carro)))

#ADICIONANDO ITENS

carro["Cambio"]="Automatico"
print(carro)
print("")
del carro["Cambio"]
print(carro)
 
 
 
    
