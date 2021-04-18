#Create a distionary of hindi words with values as their english translation. Provide user with an option to look it up
myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Items"
}
print("Options are:",myDict.keys())
a = input("Enter the hindi word\n")
#print("Meaning of your word is:", myDict[a])

#Below line will not throw an error if key is not present in the dictionary
print("Meaning of your word is:", myDict.get(a))