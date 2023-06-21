from __future__ import barry_as_FLUFL


carros=["HRV","Polo","Jetta","Cruze","Fusion"]

itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except:
        print("Fim da lista")