# Object of a Class

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
