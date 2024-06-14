#PROCEDURAL VS OBJECT ORIENTED PROGRAMMING->PROCEDURAL->C,VISUAL BASIC,TOP DOWN APPROACH,DIVIDED INTO FUNCTIONS AND
# WORKS BASED ON PROCEDURE
#->OOPS->C++,JAVA,BOTTOM UP APPROACH,EMPHASIS ON DATA

class Cars():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
    def price_inc(self):
        self.price=int(self.price*1.15)

honda=Cars('city','2017',100000)
tata=Cars('bolt','2017',500000)
honda.modelname='city'
honda.yearm='2017'
honda.price=100000

tata.modelname='bolt'
tata.yearm='2017'
tata.price=600000

print(honda.price)
honda.price_inc()
print(honda.price)

"""INHERITENCE"""
# It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class.


# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()


"""super function"""
#The super() function is a built-in function that returns the objects that represent the parent class. It allows to access the parent class’s methods and attributes in the child class.
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)


obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
"""type of inheritence-"""#->Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
#Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.
#Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
#Hierarchical inheritance More than one derived class can be created from a single base.
#Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one
# type of inheritance.





"""POLYMORPHISM"""
#The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.

class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

"""ENCAPSULATION"""
# It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.


"""ABSTRACTION"""#->Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."
# Python program demonstrate
# abstract base class work
from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()



"""OVERRIDING"""
#Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
