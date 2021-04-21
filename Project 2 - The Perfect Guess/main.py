'''We are going to write a program that generates a random number and asks the user to guess it.
If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
Similarly, if the user’s guess is too low, the program prints “higher number please”.
When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
Hint: Use the random module'''

import random
randNumber = random.randint(1, 10)
# print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Hint: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong. Enter a smaller number")
        else:
            print("You guessed it wrong. Enter a larger number")
        
    
print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You broke the highscore")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))