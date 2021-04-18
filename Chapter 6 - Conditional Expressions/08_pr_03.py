#A spam comment is defined as a test containing following keywords:
# "make a lot of money","buy now","subscribe this","click this"
# Wring a program to detect these spams 

text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now"):
    spam = True
elif("click this"):
    spam = True
elif("subscribe this"):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")


