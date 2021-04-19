f = open('sample.txt')
#Read First Line
data = f.readline() #Readline function is used to read one full line at a time
print(data)

#Read Second Line
data = f.readline()
print(data)

#Read Third Line
data = f.readline()
print(data)
f.close()