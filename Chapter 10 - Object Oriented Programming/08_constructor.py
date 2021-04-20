class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"Name of employee is {self.name}")
        print(f"Salary of employee is {self.salary}")
        print(f"Subnit of employee is {self.subunit}")

    def getSalary(self, signature):
        #print("Salary is 100k")
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning")

    @staticmethod
    def time():
        print("The time is 8AM")

#root = Employee() --> Throws Erroe 
root = Employee("Root", 500, "Youtube")
root.getDetails()
