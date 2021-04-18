#Find weather a given username contains less than 10 characters or not

username = input("Enter the username: ")
if(len(username)<10):
    print("Username is Less than 10 Characters")
else:
    print("Username is Greater than 10 Characters")