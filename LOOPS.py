#pre and pro test loops ->condition checked before or after
import random

"""WHILE"""
i=0
while(i<9):
    print(i)
    i+=1
print('goodbye')

ans=0
x=random.randint(1,20)
print(x)
while x!=ans:
    ans = int(input("enter a number"))
    if ans>0:
        if ans>x:
            print("Number is too large")
        elif ans<x:
            print("Number is too small")
    else:
        print("Sorry that you are giving up")
        break
else:
    print("Congratulations you made it")


"""FOR"""
fruits=['Mango','Banana','Grapes']
for fruit in fruits:
    print("current fruit",fruit)


"""FACTORIAL LOOP"""
num=int(input("Enter the number you want the factorial of"))
factorial=1
for i in range(2,num+1):
    factorial=factorial*i
print(factorial)


"""NESTED LOOP"""
#WRITE PYTHAGOREAN NUMBERS IN A GIVEN RANGE OF VALUES

from math import sqrt
n =int(input("Maximal Number? "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square =a**2 +b**2
        c = int(sqrt(c_square))
        if ((c_square -c**2) == 0):
            print(a, b, c)


#WAP TO ...
travelling =input("yes or no:")
people=dict()
while travelling =='yes':
    num =int(input("number of people travelling:"))
    for num in range(1, num + 1):
        name= input ("Name:")
        age =input("Age:")
        sex= input ("Male or Female:")
        x=[name,age,sex]
        people[num]=x
    travelling =input("Oops! forgot someone")
print(people)

 