"""MAP FUNCTION"""
#applies a given function to each iterable and give a new list
def new(a):
    return a*a
x=map(new,[1,2,3,4])
print(x)
print(tuple(x))

"""FILTER FUNCTION"""
def new1(i):
    if(i>=3):
        return i
j=filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))


# """REDUCE FUNCTION"""->all iterables are reduced to a single value
from functools import reduce
def a(x,y):
    return x+y
s=reduce(a,[1,3,4,5,6,7,7,8])
print(s)



"""filter with map"""
c=map(lambda x:x+x,filter(lambda x:(x>=4),[2,3,4,5]))
print(tuple(c))

"""map with filter"""
d=filter(lambda x:x+x,map(lambda x:(x>=4),[2,3,4,5]))
print(tuple(d))

"""map and filter within reduce"""
r=reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda x:(x<=4),[1,2,3,4,5,6])))
print(r)