myDict = {
    "Fast" : "Fast Learner in a quick manner",
    "Root" : "A Coder",
    "Marks" : [1,2,5],
    "anotherdict" : {'root':'Player'}
}

print(myDict['Fast'])
print(myDict['Root'])
myDict['Marks'] = [777,55]
print(myDict['Marks'])
print(myDict['anotherdict']['root'])