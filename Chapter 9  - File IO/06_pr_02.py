#The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file “Highscore.txt” which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hi-score whenever game() breaks the High-Score.

def game():
    return 655 

score = game()
with open("highscore.txt") as f:
    highscoreStr = f.read()
if highscoreStr=='':
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif int(highscoreStr)<score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))

        