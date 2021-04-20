class Employee:
    company = "Google"
    def getSalary(self, signature):
        #print("Salary is 100k")
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning")

root = Employee()
root.salary = 100000
root.getSalary("Thanks")
# Employee.getSalary(root) 
root.greet()
