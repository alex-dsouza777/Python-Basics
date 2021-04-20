class Employee:
    company = "Google"
    salary = 100

root = Employee()
stark = Employee()

#Creating instance attribute salary for both objects
# root.salary = 500
# stark.salary = 700

print(root.salary)
print(stark.salary)

# Below line throws an error as address is not present in instance/class
# print(root.address)