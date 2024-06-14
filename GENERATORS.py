#GENERATORS->FUNCTIONS THAT RETURN TRAVERSABLE OBJECTS , PRODUCE ITEMS ONE AT A TIME UNLIKE A NORMAL FUNCTION,
# RUN ALONG WITH FOR LOOPS
def new(dict):
    for x,y in dict.items():
        yield(x,y)
a={1:"Hi",2:"WELCOME"}
b=new(a)
print(b)
print(next(b))
print(next(b))
# print(next(b))=>stop iteration has been called

def myfunc(i):
    while i<=3:
        yield i
        i+=1
j=myfunc(2)
print(next(j))

def ex():
    n=3
    yield n
    n=n*n
    yield n
v=ex()
for x in v:
    print(x)


#Generator expressions
f=range(6)
print("list comp",end=":")
q=[x+2 for x in f]
print(q)
print("gen exp",end=":")
r=(x+2 for x in f)
print(r)
for x in r:
    print(x)

"""USE CASES"""
#fibonacci series
def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
    print(x,end=" ")


#number stream
a=range(100)
b=(x for x in a)
for y in b:
     print(y)

#Sinewave using seaborn
import numpymodule as np
from matplotlibmodule import pyplot as plt
import seaborn as sb
def s(flip=2):
    x=np.linspace(0,14,100)
    for i in range(1,10):
        yield (plt.plot(x,np.sin(x+i*.5)*(7-i)*flip))
sb.set()
s=s()

print(next(s))
print(next(s))
plt.show()