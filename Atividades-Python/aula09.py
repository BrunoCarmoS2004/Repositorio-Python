from traceback import print_tb


a=10
b=5
op="*"
res=0

op = input("Escreva qual operão você quer")  

if op=="+":
    res=a+b

elif op=="-":
    res=a-b

elif op=="*":
    res=a*b
    
elif op=="/":
    res=a/b
    
else:
    print("VOCE É UM BOBÃO")
print(str(a) + op + str(b) + "=" + str(res))

clima="Sol"
lugar=""
dinheiro=500

if clima=="Sol" and (dinheiro>=300 and dinheiro<=500):
    lugar="Clube"
    
else:
    lugar="cinema"
    
print("Vou ao "+lugar)
    


