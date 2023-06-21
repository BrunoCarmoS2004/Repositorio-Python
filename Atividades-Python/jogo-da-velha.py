import os
import random

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogada=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print("    0   1   2")
    print("0:  "+velha[0][0]+" | "+ velha[0][1]+" | "+velha[0][2])
    print("   -----------")
    print("1:  "+velha[1][0]+" | "+ velha[1][1]+" | "+velha[1][2])
    print("   -----------")
    print("2:  "+velha[2][0]+" | "+ velha[2][1]+" | "+velha[2][2])
    print("Jogadas "+ str(jogadas))

def jogadorjoga():
     global jogadas
     global quemJoga
     global vit
     global maxJogada
     
     if quemJoga == 2 and jogadas < maxJogada:
        
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
            while velha[l][c] != " ":
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e ou coluna invalida")
            os.system("pause")

def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogada
    if quemJoga == 1 and jogadas < maxJogada:
        l=random.randrange(0,3)
        c=random.randrange(0,3) 
        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        quemJoga=2
        jogadas+=1

def verificarVitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1       
            if(soma==3):
                vitoria=s
                break
            il+=1  
        if(vitoria!="n"):
            break
        #Verificar Coluna
        il=ic=0
        while ic<3:
            soma=0
            il=0
            while il<3:
                if(velha[il][ic]==s):
                    soma+=1
                il+=1 
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        #diagonais 1
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
                    soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
        #diagonais 2
        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if(velha[idiagl][idiagc]==s):
                    soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global jogadas
    global quemJoga
    global maxJogada
    global vit
    global velha
    jogadas=0
    quemJoga=2
    maxJogada=9
    vit="n"
    velha=[
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
        
while True:
    tela()
    jogadorjoga()
    cpuJoga()
    tela()
    vit=verificarVitoria
    #if (vit!="n" or jogadas >=maxJogada:
        #break
    
    
