# Mutators and Accessors 
# Methods of Data Hiding
# Mutators are methods that change the value of an attribute also known as setters
# Accessors are methods that return the value of an attribute also known as getters

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
person1 = Person("John", 36)
print(person1.get_name())
print(person1.get_age())

person1.set_name("Jack")
person1.set_age(40)
print(person1.get_name())
print(person1.get_age())