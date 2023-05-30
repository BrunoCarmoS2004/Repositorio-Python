import os
os.system('cls')

def somar(n1,n2):
    
    print("Curso de python do Youtube")
    n3 = n1 + n2
    print(n3)
    
def textos(*txt):
    for t in txt:
        print(t)
        
def somar2(*num):
    r=0
    for n in num:
        r+=n
    print(r)
    
    
valores=[1,5,3,2]       
def vetor(valores):
    t=0
    for n in valores:
        t+=n
    print(t)    
    
somar(10,5)
somar(85,5)
somar(78,99)
print("")
print("")
textos("Bruno","Rafael","Gabriel","Joao","lucas")
print("")
print("")
somar2(78,99,0,5,6,7,12,34,55,667,127)
print("")
print("")
vetor(valores)