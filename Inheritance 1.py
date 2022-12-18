# Object of a Class

# __init__ is a constructor. It is used to initialize the object of a class.
# self is a keyword which is used to refer to the current object of a class.

# Inheritance is a process of creating a new class from an existing class.
# Super Class: The class from which we are inheriting is called Super Class.
# Sub Class: The class which is inheriting is called Sub Class.

# There are two types of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance

# Single Inheritance : When a class inherits from only one class, it is called Single Inheritance.
# Multiple Inheritance : When a class inherits from more than one class, it is called Multiple Inheritance.


class A:
    def __init__(self):
        print("I am in A init")

    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")
        
class B:
    def __init__(self):
        print("I am in B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")
        
a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature4()

class C(B):
    def __init__(self):
        super().__init__()
        print("I am in C init")
        
c1 = C()

class D(A,C):
    def __init__(self):
        super().__init__()
        print("I am in D init")
        
d1 = D()
    

