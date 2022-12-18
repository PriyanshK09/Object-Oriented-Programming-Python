class Vehicle:
    def seating_capacity(self):
        return f"The seating capacity of a Car is 4 passengers"

class Car1(Vehicle):
    pass

class Car2(Vehicle):
    pass

class Bus1(Vehicle):
    def seating_capacity(self):
        return f"The seating capacity of a bus is 50 passengers"
    
obj = Vehicle()

obj1 = Car1()
obj2 = Car2()
obj3 = Bus1()

print(obj1.seating_capacity())
print(obj2.seating_capacity())
print(obj3.seating_capacity())
    