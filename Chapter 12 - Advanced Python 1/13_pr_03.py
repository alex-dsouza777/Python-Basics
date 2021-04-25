#Write a list comprehension to print a list that contains the multiplication table of a user-entered number.

num = int(input("Enter Your Number: "))

table = [num * i for i in range(1, 11)]
print(table)