a = 54 #Global Variable
def func1():
    global a
    print(f"Print Statement 1: {a}")
    a = 8 #Local Variable
    print(f"Print Statement 2: {a}")

func1()
print(f"Print Statement 3: {a}")