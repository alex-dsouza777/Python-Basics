#Create a class programmer for storing information of a few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the company is {self.company} and the Programmer is {self.name} and product is {self.product}")
        
root = Programmer("root", "GitHib")
stark = Programmer("stark", "Skype")
root.getInfo()
stark.getInfo()