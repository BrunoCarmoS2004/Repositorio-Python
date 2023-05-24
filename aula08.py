carros=["HRV","Golf","Argo","Focus"]
carros.append("Fit")
carros.append("Fusion")
carros.append("ka")

print(str(len(carros))+" Todos os carros da lista")

print(carros)

carros.remove("Fusion")

print(carros)

print(str(len(carros))+" Todos os carros da lista")

carros.pop()
print(carros)
print(str(len(carros))+" Todos os carros da lista")

del carros[2]

print(carros)
print(str(len(carros))+" Todos os carros da lista")
carros2=list(carros)

carros3=["Fiesta","Windows","Opala"]
carros4=carros+carros3

carros.clear()

print("Banana")

print(carros2)






print(str(len(carros4))+" Todos os carros da lista")
print(carros4)
