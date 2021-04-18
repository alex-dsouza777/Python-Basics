#Creating empty set
b = set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) #Set is a collection of non repatative items so it will print 5 only once
b.add(5)
b.add(5)
b.add((4,5,6)) #You can add touple in set
#b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

#Length of set
print(len(b)) #Prints the lngth of the set

#Removal of items
b.remove(5) #removes 5 from set b
#b.remove(10) #throws an error because 10 is not present in the set
print(b)

print(b.pop())
print(b)