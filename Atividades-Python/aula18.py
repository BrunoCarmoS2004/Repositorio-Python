from ast import expr
from cProfile import label

soma=lambda a,b: a+b

mult=lambda a,b,c:(a+b)*c

r=soma(2,5)
print(r)
print()
print()
print(mult(2,4,10))
print()
print()
print((lambda a,b:a+b)(3,2))
