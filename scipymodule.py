#to solve scientific and mathematical problems.Built on numpy.manipulation and visualisation
#diff bw numpy and scipy
#NumPy and SciPy used for mathematical and numerical analysis
# NumPy contains array data and basic operations
# SciPy consists of all the numerical code
# SciPy contains fully-featured versions of mathematical
# and scientific functions


#basic functions->help(),info(),source()
from scipy import cluster  #cluster->subpackage
help(cluster)
# help()
import scipy
# scipy.info(cluster)
# scipy.source(cluster)


"""SPECIAL FUNCTIONS"""
from scipy import special
#exponential f
a=special.exp10(2)
print(a)
#sincosfunc
print(special.sindg(90))
print(special.cosdg(90))


"""integration"""
from scipy import integrate
#quad for 1 variable
i=scipy.integrate.quad(lambda x:special.exp10(x),0,1)  #0,1->ll,ul
print(i)
#dblquad for double integral
e=lambda x,y:x*y**2
f= lambda x:1
g=lambda x:-1
print(integrate.dblquad(e,0,2,f,g))


"""FOURIER TRANSFORMATIONS"""
# https://realpython.com/python-scipy-fft/->to understand fourier
from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=ifft(x)
print(y)



"""LINEAR ALGEBRA"""
from scipy import linalg
a=np.array([(1,2),(3,4)])
b=linalg.inv(a)
print(b)

"""INTERPOLATION"""#->new data points with existing ones
import matplotlib.pyplot as plt
from scipy import interpolate
x=np.arange(5,20)
y=np.exp(x/3.0)
f=interpolate.interp1d(x,y)      #interp1d->to interpolate a 1d function
x1=np.arange(6,12)
y1=f(x1)
plt.plot(x,y,'o',x1,y1,'--')
plt.show()
