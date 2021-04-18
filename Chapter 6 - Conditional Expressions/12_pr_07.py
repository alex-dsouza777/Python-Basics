#Find out weather a given post is talking about "root" or not

post = ("Hello root how are you?")
input = input("Enter the word\n")
if(input in post):
    print("present")
else:
    print("not present")