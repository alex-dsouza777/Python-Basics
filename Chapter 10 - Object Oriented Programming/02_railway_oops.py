import pandas as pd 

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

rootApplication = RailwayForm()

rootApplication.name = "Root"
rootApplication.train = "Pune"
rootApplication.printData()