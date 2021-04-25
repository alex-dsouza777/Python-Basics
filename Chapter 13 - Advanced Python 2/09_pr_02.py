#Write a program to input name, marks and phone number of a student and format it using the format function like below:
# “The name of the student is Root, his marks are 72 and the phone number is 99999888”

name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
phone = int(input("Phone Number: "))

template = "The name of the student is {} his marks are {} and phone is {}"
output = template.format(name, marks, phone)
print(output)