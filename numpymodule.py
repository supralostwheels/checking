#why use numpy over list->less memory , faster, convenient
import numpy as np
a=np.array([1,2,3])
b=np.array([(1,2,3),(4,5,6)])
import time,sys

s=range(1000)
print(sys.getsizeof(5)*len(s))    #finding size of s,5 is any 1 element of s
x=np.arange(1000)
print(x.size*x.itemsize)    #x.size->no of element itemsize->1 element size


size=100000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
start=time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)#->for range
start=time.time()
result=a1+a2
print((time.time()-start)*1000)#->for numpy

#dimension of an array,size and all
a=np.array([(1,2,3),(4,5,6)])
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)

#reshaping
a=np.array([(1,2,3),(4,5,6),(7,8,9)])
# a=a.reshape(3,2)

#slicing
print(a)
print(a[0,2])
print(a[0:2,2])

#linespace
a=np.linspace(1,3,10)#->10 equally spaced numbers between 1 and 3
print(a)

#sum.max,min
a=np.array([1,2,3])
print(a.sum())
print(a.max())


#axis
a=np.array([(1,2,3),(4,5,6)])
print(a.sum(axis=0))
print(a.sum(axis=1))

#square root and deviation
print(np.sqrt(a))
print(np.std(a))

#operations
a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
c=np.array([(1,2),(4,5)])
print(a+b)#other operations as well

#concatenation(stacking)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

#ravel
print(a.ravel())

import matplotlib.pyplot as plt
import numpy as np

#sin cos functions
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y)
plt.show()

#exp and log functions
ar=np.array([1,2,3])
print(np.exp(ar))
print(np.log(ar))
print(np.log10(ar))

