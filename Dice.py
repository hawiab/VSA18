import random
P1Counter = 0
P2Counter = 0
PlayAgain = 1
Odd = [1,3,5]
Even = [2,4,6]
while int(PlayAgain) != 0:
    if int(PlayAgain) == 1:
        print "Welcome to Chance!"
        Roll = raw_input("How many times would you like to roll? ")
        Counter = 0
        if Counter <= Roll:
            for item in range(int(Roll)):
                RandomNum = random.randint(1, 6)
                if RandomNum in Odd:
                    P1Counter = P1Counter + 1
                    Counter = Counter + 1
                else:
                    P2Counter = P2Counter + 1
                    Counter = Counter + 1
        elif Counter >= Roll:
            print"Player 1: You have", P1Counter, "point(s). Player 2: You have", P2Counter, "point(s)."
            break
    PlayAgain = raw_input("Would you like to play again? 1 for yes, 0 for no. ")