#Function to remove a given word from a list and strip it at the same time.

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "  Root is a Computer  "
n = remove_and_split(this, "Root")
print(n)