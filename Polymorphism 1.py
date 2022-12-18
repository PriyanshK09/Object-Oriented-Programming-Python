# Polymorphism

a = "Hello"
b = [1,2,3,4,5,6]

print(len(b))

# Polymorphism with class methods, Calculation of area of rectangle/square

class Rect:
    
    def calculateArea(self, l=None, b=None):
    
        if l != None and b != None:
                return l*b
            
        elif l != None:
                return l*l
    
obj = Rect()
print(obj.calculateArea(5, 6))
print(obj.calculateArea(5))

