#Accept marks of students and display them in sorted manner

m1 = int(input("Marks for student 1: "))
m2 = int(input("Marks for student 2: "))
m3 = int(input("Marks for student 3: "))
m4 = int(input("Marks for student 4: "))

myList = [m1,m2,m3,m4]
myList.sort()
print(myList)