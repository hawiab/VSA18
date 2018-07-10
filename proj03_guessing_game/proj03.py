# Name: Hawi, Belal, Ryan
# Date: 07/10/18


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
random_number = random.randint(1,9)
counter = 0
print ("Im thinking of a number between 1 and 9. Can you guess my number?")
for counter in range (1, 4):
    Guess = raw_input("Enter a number, or '0' to end the game: ")
    if int(Guess) == 0:
        print("Wimp!")
        break
    elif int(Guess) < random_number:
        print "Your number is too low!"
    elif int(Guess) > random_number:
        print "Your number is too high!"
    elif int(Guess) == random_number:
        print "Congratulations, you guessed my number! You used ",counter, " guesses"
    if counter == 3:
        print("You ran out of guesses! Idiot!")

