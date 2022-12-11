class Car:
    
    wheels = 4 # Class variable (static variable)
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
product1 = Car("Ford", "Mustang", 1964)
product2 = Car("Chevy", "Camaro", 1969)
product3 = Car("Dodge", "Charger", 1970)

print(product1.make)
print(product2.model)
print(product3.year)
print(product1.wheels)