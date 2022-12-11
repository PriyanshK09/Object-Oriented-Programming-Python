class Person:
    def __init__(self):
        self.name = "John"
        self.age = 23
        
    def updateName(self, name):
        self.name = name
        
    def compareAge(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
person1 = Person()
person2 = Person()

person1.updateName("Jack")
print(person1.compareAge(person2))
