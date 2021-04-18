#Find out weather a given name is present in a list or not

names = ["root", "groot", "strak"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")