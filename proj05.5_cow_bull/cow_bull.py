# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.


import random
Number = str(random.randint(1000, 9999))  # random 4 digit number
NumBlank = len(Number) * "_"
NumLength = len(Number)
Yes = ""
print "Welcome to the cows and bulls game!"
print Number
while Yes != "No":
    Counter = 0
    Cow = 0
    Bull = 0

    UserNum = raw_input("Enter a number: ")
    if UserNum == Number:
        print "Congratulations! You did it! The number is",Number
    else:
        while Counter < 4:
            if UserNum[Counter] in Number:
                if UserNum[Counter] == Number[Counter]:
                    Cow = Cow + 1
                    Counter = Counter + 1
                else:
                    Bull = Bull + 1
                    Counter = Counter + 1
            Counter = Counter + 1
            print "You have", Cow, "cows and",Bull,"bulls."

