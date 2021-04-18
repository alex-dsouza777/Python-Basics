#Find sum of natural numbers upto n using recursion
 
def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)

n = 10
print(recurSum(n))

