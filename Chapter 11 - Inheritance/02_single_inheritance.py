''' SINGLE INHERITANCE '''

#Base Class
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")

#Child Class
class Programmer(Employee):
    language = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"Language is {self.language}")

    
    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)