#Create a class with a class attribute a; 
# create an object from it and set a directly using object.a=0 Does this change the class attribute?


class Sample:
    a = "Root"

obj = Sample()
obj.a = "Stark"
#Sample.a ="Stark"

print(Sample.a)
print(obj.a)