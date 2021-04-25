name = "root"
company = "Google"
Type = "Coding"
#a = f"This is {name}"
# a ="This is {}".format(name)
#a ="This is {} and his company is {}".format(name, company)
a ="This is {1} and his {2} company is {0}".format(name, company, Type)
print(a)