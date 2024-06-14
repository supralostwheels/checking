#arrays are data structures which can hold more than one value at a time. A collection of order values of the same data type with contiguous memory locations
import array as arr #to use array
a=arr.array("i",[1,2,3,4,5,6])  #array is the constructor i is for integer, d is for decimal
print(a)
#for accessing array elements use indexes.negative indexing starts from right side from -1
"""ACCESSING ELEMENTS"""
print(a[1])
"""Finding length"""
len(a)
"""ADDING ELEMENTS"""
a.append(8)
print(a)
a.extend([8,7,6,5])
print(a)
a.insert(2,6)
print(a)

"""REMOVING ELEMENTS"""
#pop can have either no or 1 parameter.returns the removed value.Without a parameter it removes last element.For 1 parameter it takes the index value to be removed
#remove has 1 parameter.Returns nothing.Removes the first occurence of the given value

x=a.pop()
print(a)
y=a.pop(2)
print(a)
a.remove(8)
print(a)


"""ARRAY CONCATENATION"""
b=arr.array("i",[1,2,3,4,5,6])
c=arr.array("i",[1,2,3,4,5,6])
d=arr.array("i")
d=b+c
print(d)

"""SLICING AN ARRAY"""
#Returns a range of elements but not the last index
print(d[0:10])
print(d[::-1])  #we do not use this as it exhausts teh memory


"""LOOPING AN ARRAY"""
"""for loop"""
for v in d[0:-3]:
    print(v)

"""While loop"""
temp=0
while temp<len(d):
    print(a[temp])
    temp+=1


