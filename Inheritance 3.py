
class A:
    def __init__(self):
        print("This is init of method A")

    def method1(self):
        print("This is method 1")

class B:
    def __init__(self):
        # super().__init__()
        print("This is init of method B")

    def method2(self):
        print("This is method  2")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("This is init of method 3")

    def method3(self):
        print("This is method 3")

objC = C()

