#Write a program to filter a list of numbers that are divisible by 5.

l = [1, 2, 3, 4, 5, 66, 50, 20, 7, 88, 77, 76, 70, 55, 40]

a = filter(lambda a: a%5 == 0, l)
print(list(a))