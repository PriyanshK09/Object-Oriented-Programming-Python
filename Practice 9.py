# Static Variables
# Decorators and Static Variables in Python 

# Static Variables are variables that are shared by all instances of a class.

class MyClass:
    x = 10

    def __init__(self):
        self.y = 20

    def method(self):
        print(self.x, self.y)
        
obj1 = MyClass()
obj2 = MyClass()

obj1.method()
obj2.method()

# Output:
# 10 20