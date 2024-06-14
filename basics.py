#interpretor is a program that connects your program with the database to have it working
#IDE (Integrated Development Environment) is a GUI(Graphical User Interface) where programmers write their code and produce the final products.
#Difference between ide and code editors is that code editors is only for code editing and manipulation whereas ide helps in complete software developement

"""VARIABLES AND DATA TYPES"""
#Variable is a memory location thta stores a value.They are case sensitive
#Data types are ->
#Numbers->integer,float,boolean,complex
#integer
x=10
print(type(x))
#float
x=20.6
print(type(x))
#complex
x=10j
print(type(x))
#boolean
x=10>9
print(type(x))


#string
name="jas"
len(name)
name[2]
# name[2]=d as a string is immutable
name.upper()
name.lower()
name[-2:]



#list     #can have different data types and is mutable
list1 = [1, 2, 3]
list1.append(4)
print(list1)
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
list1 = [1, 2, 3]
list1.insert(1, 4)  #insert 4 on 1st index
print(list1)
list1 = [1, 2, 3, 4]
list1.remove(3)
print(list1)
list1 = [1, 2, 3, 4]
element = list1.pop()
print(element)
print(list1)
list1 = [1, 2, 3, 4, 5]
list2 = list1[1:3]
print(list2)
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print(list1)
list1 = [1, 2, 3, 4, 5]
length = len(list1)
minimum = min(list1)
maximum = max(list1)
print(length)
print(minimum)
print(maximum)


#dictionary->Python allows you to associate a key with a value. It is like a real dictionary, where each word would be the key and the definition of the word would be the value.
# Each key in a Python dictionary must be unique. All keys must be the same data type (for example, all strings or all numbers), but the values can be of any data type.
student = {'Firstname': 'Sam', 'Lastname': 'Taylor', 'Age': 15}
print(student['Firstname'])

csDict = {'alu': 'arithmetic logic', 'binary': 'counting system of 0,1', 'compiler': 'converts instructions into machine code'}
print(csDict['alu'])
csDict['alu'] = 'Arithmetic Logic Unit'
print(csDict['alu'])

csDict = {'alu': 'arithmetic logic unit', 'binary': 'counting system of 0,1', 'compiler': 'converts instructions into machine code'}
csDict['debugger'] = 'Tool to test and debug programs'
print(csDict)

csDict = {'alu': 'arithmetic logic unit', 'binary': 'counting system of 0,1', 'compiler': 'converts instructions into machine code'}
del csDict['alu']
del csDict['compiler']
print(csDict)

csDict = {'alu': 'arithmetic logic unit', 'binary': 'counting system of 0,1', 'compiler': 'converts instructions into machine code'}
print(len(csDict))

csDict = {'alu': 'arithmetic logic unit', 'binary': 'counting system of 0,1', 'compiler': 'converts instructions into machine code'}
print('binary' in csDict)
print('bin' in csDict)


#tuples->Tuples are like lists. The difference is that tuples are immutable
student = ('Sam', 'Taylor', 15, 'Reading', 'Berkshire')
print(student[3])

student = ('Sam', 'Taylor', 15, 'Reading', 'Berkshire')

for item in student:
   print(item)

student = ('Sam', 'Taylor', 15, 'Reading', 'Berkshire')

firstName = student[0]
lastName = student[1]
age = student[2]
city = student[3]
county = student[4]

print('First name: ' + firstName)
print('Age: ' + str(age))

student = ('Sam', 'Taylor', 15, 'Reading', 'Berkshire')
print(len(student))

#sets->Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}#True and 1 is considered the same value:
print(thisset)

my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)


"""TYPE CONVERSION"""
#x=10+"name" wont take place as diff data types so we will do type conversion
str(10)+"name"



