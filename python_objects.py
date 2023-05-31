class Student:
    def __init__(self,name,grades): #a function inside a class is called a method
        self.name=name
        self.grades=grades
    def average_grade(self):
        return sum(self.grades)/len(self.grades)

student=Student("Bob",(90,90,93,78,60))#pass the parameters initialized in the __init__method

student2=Student("Rolf",(90,50,93,78,60))

print(student.name)
print(student.grades)
print(student.average_grade())#call average class method

print(student2.name)
print(student2.average_grade())