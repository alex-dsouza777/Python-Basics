#Factorial of a given number using for loop

#n! = 1 x 2 x 3 x .. xn
num = int(input("Enter the number "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"Factorial is {factorial}")