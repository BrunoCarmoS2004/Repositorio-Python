import random
import os

os.system('cls')
continuar = "sim"
while (continuar == "sim"):
    os.system('cls')
    erros=0
    sortiado=random.randrange(0,100)
    jogador=int(input("Degite seu numero..: "))

    while (sortiado != jogador):
        os.system('cls')
        if(sortiado > jogador):
            print("Errou! o numero sortiado é maior")
        elif(sortiado < jogador):
            print("Errou! o numero sortiado é menor")
        erros+=1
        jogador=int(input("Digite seu numero..: "))
        
    print("Numero "+str(jogador)+", voce acertou o numero sortiado "+str(erros+1)+" tentativas")

    continuar=input("Deseja jogar novamente? sim ou Não..:")