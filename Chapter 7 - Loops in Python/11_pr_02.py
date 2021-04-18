#Program to greet all the person names stored in a list l1 which starts with S

l1 = ["Root","Groot","Stark","Son"]

for name in l1:
    if name.startswith("S"):
        print("Hello "+ name)