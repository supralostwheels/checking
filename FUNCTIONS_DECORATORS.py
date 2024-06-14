"""FUNCTIONS IN PYTHON"""


# FIRST CLASS OBJECT->IN PYTHON EVERYTHING IS TREATED AS AN OBJECT INCLUDING ALL THE DATA TYPES,FUNCTIONS TOO.THEREFORE A FUNCTION IS ALSO KNOWN AS A FIRST CLASS OBJECT AND CAN BE PASSED AROUND AS ARGUMENT

# INNER FUNCTION-> IT IS POSSIBLE TO DEFINE FUNCTIONS INSIDE A FUNCTION CALLED INNER FUNCTION

def func1(name):
    return f"Hello{name}"


def func2(name):
    return f"{name}, how u doin"


def func3(func4):
    return func4("dear learner")


print(func3(func1))
print(func3(func2))


def func():
    print("first function")

    def func1():
        print("first child function")

    def func2():
        print("second child function")

    func2()
    func1()


func()


def func(n):
    def func1():
        return "jasmine"

    def func2():
        return "python"

    if n == 1:
        return func1()
    else:
        return func1()


a = func(1)
b = func(2)
print(a)
print(b)

"""USING DECORATOR"""


# Decorators in python are very powerful which modify the behaviour of a function withouy modifying it permanently.it
# basically wraps another function and since both functions are callable it returns a callable
def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to the screen")

    return wrapper


def function2():
    print("jasmine")


function2 = function1(function2)
function2()


def function3(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to the screen")

    return wrapper


@function3
def function4():
    print("jasmine")


function4()

#https://www.geeksforgeeks.org/args-kwargs-python/  -->for *args,**kwargs
def g1(function):
    def wrapper1(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("welcome to the screen")

    return wrapper1


@g1
def g2(name):
    print(f"{name}")


g2("waseem")

"""FANCY DECORATORS"""


class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side**2
    @classmethod
    def unit_square(cls):
        return cls(1)
s=Square(4)
print(s.side)
print(s.area)

"""SINGLETON CLASS"""
import functools
def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance=cls(*args,*kwargs)
        return wrapper.instance
    wrapper.instance=None
    return wrapper
@singleton
class one:
    pass
first=one()
second=one()
print(first is second)



"""NESTED DECORATOS"""
import functools
def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                value=func(*args,**kwargs)
            return value
        return wrapper
    return decorator_repeat
@repeat(num=5)
def function(name):
    print(f"{name}")
function("hi")