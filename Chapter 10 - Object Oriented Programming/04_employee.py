class Employee:
    company = "Google"
    salary = 100

root = Employee()
stark = Employee()
root.salary = 500
stark.salary = 700

print(root.company)
print(stark.company)

Employee.company = "YouTube"
print(root.company)
print(stark.company)
print(stark.salary)
print(root.salary)
