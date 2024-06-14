"""ARITHMETIC OPERATORS"""
X=10
Y=20
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X//Y)  #float division
print(X%Y)  #modulus

"""ASSIGNMENT OPERATORS"""
x=10
x-=6
x/=2

"""COMPARISN OPERATORS"""
val=10
num=20
compare=val==num #>,<,etc

"""CONDITIONAL STATEMENTS"""
if val==num:
    print('equal')
elif val>num:
    print('greater')
else:
    print('greater')

"""LOGICAL OPERATORS"""
#NAO->NOT AND OR->preference order

"""IDENTITY OPERATORS"""
#object should be same
x=10
y=10
print(x is y)
x=[1,2,3]
y=[1,2,3]
print(x is y)
print(x==y)


"""BITWISE OPERATORS"""
#works on bits
print(10&12)
print(10|12)
print(10>>12)#RIGHT SHIFT
print(10<<12)#LEFT SHIFT
print(10^12)#XOR
print(~12)#NOT


