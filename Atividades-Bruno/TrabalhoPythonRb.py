cardápio = ["Bolo", "Laranja", "Uva"]

resposta = 0
while resposta != 5:
    print("--------------------------------------------------")
    print("|          O que você gostaria de fazer?         |")
    print("--------------------------------------------------")   
    print("|                1 - ver cardápio                |")
    print("|                2 - remover item                |")
    print("|              3 - adicionar um item             |")
    print("|           4 - Buscar item por número           |")
    print("|                    5 - sair                    |")
    print("--------------------------------------------------")
    resposta = int(input(" resposta: "))
    print()
    print("--------------------------------------------------")
    
    if resposta == 1:
        j = 1
        print()
        print(" Cardápio: ")
        print()
        for i in cardápio:
            print(" ",j,"-",i)
            j = j + 1
        print()
        print("--------------------------------------------------")
        print()
        print("           Pressione <Enter> para voltar          ")
        print()
        input("--------------------------------------------------")
        print()

    if resposta == 3:
        print()
        print(" Qual item você gostaria de adicionar? ")
        print()
        item = input(" resposta: ")
        print()
        cardápio.append(item)
        print("--------------------------------------------------")
        print()
        print("            Item adicionado ao cardápio           ") 
        print("           Pressione <Enter> para voltar          ")
        print()
        input("--------------------------------------------------")
        print()
        
    if resposta == 2:
        j = 1
        print()
        print(" Qual item você gostaria de retirar?")
        print()
        for i in cardápio:
            print(" ",j,"-",i)
            j = j + 1
        print()
        item = int(input("resposta: "))
        print()
        del cardápio[item-1]
        print("--------------------------------------------------")
        print()
        print("             Item removido do cardápio            ")
        print("         pressione <Enter> para continuar         ")
        print()
        input("--------------------------------------------------")
        print()
    
    if resposta == 4:
        print()
        print("Escolha um item: ")
        j = 1
        print()
        for i in cardápio:
            print(" Item ",j)
            j = j + 1
        print()    
        item = int(input(" resposta: "))
        print()
        print(" O item equivalente a esse número é",cardápio[item-1])
        print()
        print("--------------------------------------------------")
        print()
        print("       Pressione <Enter> para voltar            ")
        print()
        input("--------------------------------------------------")
        print()

