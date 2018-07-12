# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!




y = ""
while y != "N" and y != "No":
    word = choose_word(wordlist)
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    c = 0

    print '''
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                    |___/                       
        '''
    print "Welcome to the game, Hangman!"
    while True:
        try:
            guesses = int(raw_input("How many guesses would you like? "))
            break
        except ValueError:
            print "Please use a valid input"
    twoplayer = raw_input("1 or 2 players? ")
    if int(twoplayer) == 2:
        while c != 80:
            word = raw_input("Player 1. Choose your word: ")
            word = word.lower()
            word = word.replace(" ", "")
            if word in wordlist:
                print "CHEATER! You thought you were slick?"
                while c != 80:
                    print
                    c = c+1
            else:
                print "Use a real word please. Choose again."
    print "I am thinking of a word that is", len(word),"letter(s) long."
    wordblank = ["_ "] * len(word)
    wordlength = len(word)

    while True:
        if wordlength == 0:
            print "------------------------------"
            print
            print "            You've escaped death."
            print '''
                     _
                   _|_|_
                    (_)
                    \|/
                     |
                    / \\
            '''
            print "Congratulations! You won the game! The word was ""'"+word+"'."
            break
        elif guesses == 0:
            print "------------------------------"
            print '''
                 _______
                |/     |
                |     (_)
                |     \|/
                |      |
                |     / \\
                |
                |___
            '''
            print "Good try. The word is ""'"+word+"'."
            break
        else:
            print "------------------------------"
            counter = 0
            deleted = 0
            print "Available Letters:"," ".join(alphabet)
            print "You have", guesses ,"guess(es) left."
            letter = raw_input("Please guess a letter or enter 'Exit' to end the game: ")
            letter = letter.lower()
            if letter in alphabet:
                    if letter in word:
                        while counter < len(word):
                            if letter == word[counter]:
                                wordlength = wordlength - 1
                                wordblank[counter] = letter + " "
                                if deleted == 0:
                                    alphabet.remove(letter)
                                    deleted = 1
                            counter = counter + 1
                        print "Good Guess:", "".join(wordblank)

                    else:
                        print "Oops, that letter isn't in the word:", "".join(wordblank)
                        guesses = guesses - 1
                        alphabet.remove(letter)
            elif letter == "exit":
                print "Sorry you had to go! The word was","'"+word+"'."
                break
            else:
                print "Guess again: "
    print "--------------------"
    while y != "Yes" or y != "Y" or y != "No" or y != "N":
        y = raw_input("Do you want to play again? ")
        y = y[0].upper() + y[1:].lower()
        if y == "Yes" or y == "Y":
            break
        elif y == "No" or y == "N":
            print( )
            print "Thank you for playing!"
            break
        else:
            print "Type a valid answer."

