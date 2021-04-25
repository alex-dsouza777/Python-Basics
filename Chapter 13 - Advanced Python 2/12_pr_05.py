#Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [3, 5, 1, 8, 33, 98, 35, 66]

a = reduce(max, l)
print(a)