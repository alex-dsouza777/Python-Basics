#Snake Water Gun OR Rock Paper Scissors Game

import random

def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True



print("Computers Turn : Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer = 'g'


you = input("Your Turn : Snake(s) Water(w) or Gun(g)?")
a = gameWin(computer, you)

print(f"Computer choose {computer}")
print(f"You choose {you}")

if a == None:
    print("The Game Is A Tie")
elif a:
    print("You Win")
else:
    print("you Loose")
