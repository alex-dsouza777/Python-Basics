a = [3, 4, 6, 67, 88, 9, 77, 6, 88, 123, 127, 30, 10, 97]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)

# print(b)

#Shortcut to write same as above
b = [i for i in a if i%2==0]
print(b)
