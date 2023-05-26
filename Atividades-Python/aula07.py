curso = "Curso de Python"
curso2 = "Curso de Python"
resp="Python" in curso
resp2="Python" not in curso
print(resp)
print(resp2)
print("")
print("")
print("")
print("")
############################################
texto="League of Legends"
palavra="league"
resp3 = palavra.lower() in texto.lower()
print(resp3)
############################################
coisa="Curso de Python"
canal="Bruno"
resp4=curso+" do "+ canal

print(resp4)

############################################
cidade="Bobolandia"
dia=15
mes="desembro"
ano=2019
canal="Bruno"
data=str(dia) +" de "+str(mes)+" do ano de "+str(ano)+" na cidade "+str(cidade)
print(data)

############################################
data2="{},{} de {} de {}\n -{}"
print(data2.format(dia,mes,ano,cidade,canal))