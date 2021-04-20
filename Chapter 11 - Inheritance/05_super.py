class Person:
    county = "India"

    def takeBreak(self):
        print("Take break")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreak(self):
        print("I am an Employee")

class Programmer(Employee):
    company =  "Fiverr"

    def getSalary(self):
        print("No Salary")
    
    def takeBreak(self):
        super().takeBreak()
        print("I am an Programmer")

p = Person()
p.takeBreak()

e = Employee()
e.takeBreak()

pr = Programmer()
pr.takeBreak()