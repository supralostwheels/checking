#anonymous or nameless functions
#uses->when function needed once->throw away functions,used in higher order functions(which either takes it as an
# input or gives as an output,to reduce size of code
x=lambda a:a*a
print(x(3))    #this is not the correct way to use it . Use it in a higher order function

def A(x):
    return(lambda y:x+y)
t=A(4)
print(t(8))

#filter method->filter(function,iterables)
mylist=[1,2,3,4,5,6]
newlist=list(filter(lambda a:(a/3==2),mylist))
print(newlist)

#map method->map(function,iterables)
mylist=[1,2,3,4,5,6]
p=list(map(lambda a:(a/3!=2),mylist))
print(p)

#reduce method->reduce(fuction,sequence)
from functools import reduce
print(reduce(lambda a,b: a+b,[23,56,48,91]))

#algebraic equations solving
##1
s=lambda a:a*a
print(s(4))
##2
d=lambda x,y:3*x+4*y
print(d(4,7))
##3
e=lambda a,b:(a+b)**2
print(e(2,3))