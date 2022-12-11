# Method to calculate the average of the Score 
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

student1 = Student(90, 80, 70)
student2 = Student(80, 70, 60)
student3 = Student(70, 60, 50)

print(student1.average())
print(student2.average())
print(student3.average())

# Method to calculate the average of the Score
        