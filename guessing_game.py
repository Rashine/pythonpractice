from random import randint

answer, straw, tryagain = randint(1,10), None, True
while straw != answer and tryagain:
    straw = int(input("Guess a normal number between from 1 to 10\n"))
    if straw == answer:
        print ("Got it!")
        break
    elif straw < answer:
        print ("Too low, try again!")
    else:
        print ("Too high, try again!")
    if (input ("Do you want to try again? (y/n)") != "y"):
        tryagain = False
        print ("Thanks for playing. Bye!")