class Employee:
    company = "Google"
    def getSalary(self):
        #print("Salary is 100k")
        print(f"Salary for this employee working in {self.company} is {self.salary}")

root = Employee()
root.salary = 100000
root.getSalary()

# Employee.getSalary(root) 