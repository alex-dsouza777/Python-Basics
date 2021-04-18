myDict = {
    "fast" : "Fast Learner in a quick manner",
    "root" : "A Coder",
    "marks" : [1,2,5],
    "anotherdict" : {'root':'Player'},
    1 : 2

}

#Dictionary Methods
print(myDict.keys()) #Prints the keys
print(type(myDict.keys())) #prints types
print(myDict.values()) #Shows values
print(list(myDict.keys())) #convert to list
print(myDict.items()) #Prints (keys,value) for all contents in the dictionary

print(myDict)
updateDict = {
    "friend" : "groot",
    "fruit" : "apples are fav",
    "root" : "my friend"
}
myDict.update(updateDict) #updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("root")) #Prints value associated with key root
print(myDict["root"]) #Prints value associated with key root


#The difference between .get and [] syntax in dictionaries
print(myDict.get("root2")) #Returns NONE as root2 is not present in the dictionary
print(myDict["root2"]) #throws error as root2 is not present im the dictionary