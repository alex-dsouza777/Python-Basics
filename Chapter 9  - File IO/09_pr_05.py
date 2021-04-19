#Repeat program 4 for a list of such words to be censored.

words = ["donkey", "monkey", "banana"]

with open("donkey.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "@#$@#$")
    with open("donkey.txt", "w") as f:
        f.write(content)
        