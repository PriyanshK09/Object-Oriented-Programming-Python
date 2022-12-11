# Instance Method and Class Method in Python
# Object Oriented Programming in Python
# Instance Method are the methods that are called on the object.
# Class Method are the methods that are called on the class.

class Car:
        
        wheels = 4 # Class variable (static variable)
        
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            
        def start(self):
            print("Starting the car")
            
        def stop(self):
            print("Stopping the car")
            
product1 = Car("Ford", "Mustang", 1964)
product2 = Car("Chevy", "Camaro", 1969)
product3 = Car("Dodge", "Charger", 1970)

print(product1.make) 
print(product2.model)
print(product3.year)

product1.start()
product2.stop()
