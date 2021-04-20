#Paremt 1
class Employee:
    company = "Visa"
    eCode = 100

#Parent 2
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

#Child
class Programmer(Employee, Freelancer):
    name = "Root"
 
p = Programmer()
p.upgradelevel()
print(p.company)