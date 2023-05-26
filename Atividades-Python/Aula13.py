import os
os.system('cls')
carros=[
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano",2016]
]

#print(carros[2][0])
carros.append(["Cor","Prata"])

for l,c in carros:
    print("Linha: "+l+" - Coluna: " +str(c)+"\n")
     
print("Atualizado")
    


#carros[2][1] = 2019

for l,c in carros:
    print("Linha: "+l+" - Coluna: " +str(c)+"\n")
    
    
