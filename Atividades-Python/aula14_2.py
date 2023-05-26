import os
os.system('cls')

carro={
    "Carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"Ford",
        "Modelo":"Ka"
    },
    "Carro3":{
        "Fabricante":"Volkswagem",
        "Modelo":"Golf"
    }
}

carros={
    "C":carro
}

print(carro["Carro1"])
print(carro["Carro1"]["Fabricante"])
carro["Carro1"]["Fabricante"] = "Chevrolet"
print(carro["Carro1"]["Fabricante"])
print("")
print
print(carros)