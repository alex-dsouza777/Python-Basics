#Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Enter Your Number: "))

table = [num * i for i in range(1, 11)]
print(table)
with open("tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')