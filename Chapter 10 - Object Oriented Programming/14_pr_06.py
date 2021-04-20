#Can you change the self parameter inside a class to something else (say ‘root’)?
#  Try changing self to ‘slf’ or ‘root’ and see the effects.

class Sample:
    def __init__(root, name):
        root.name = name

obj = Sample("Root")
print(obj.name)