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

# Polymorphism with Inheritance

class Bird:
    def category(self):
        print("This is the category of Bird")
        
    def fly(self):
        print("I can fly")

class Sparrow(Bird):
    pass

class Ostrich(Bird):
    def fly(self):
         print("I can't fly")

class Crow(Bird):
    pass

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()
obj_cro = Crow()

obj_spr.category()
obj_spr.fly()
obj_ost.category()
obj_ost.fly() # We can see that the method fly() is overriden in the class Ostrich due to which the output is different from the class Ostrich
obj_cro.category()
obj_cro.fly()

