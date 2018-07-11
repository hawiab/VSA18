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
while y != "n" and y != "no":
    word = choose_word(wordlist)
    guesses = 8
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    wordlength = len(word)

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(word),"letter(s) long."
    wordblank = ["_ "] * len(word)

    while True:
        if wordlength == 0:
            print "--------------------"
            print "Congratulations! You won the game! The word was", str(word) + "!"
            break
        elif guesses == 0:
            print "--------------------"
            print "Good try. The word is",word
            break
        else:
            print "--------------------"
            counter = 0
            deleted = 0
            print "Available Letters:"," ".join(alphabet)
            print "You have", guesses ,"guess(es) left."
            letter = raw_input("Please guess a letter: ")
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
            else:
                print "Guess again: "
    print "--------------------"
    while y != "yes" or y != "y" or y != "no" or y != "n":
        y = raw_input("Do you want to play again? ")
        if y == "yes" or y == "y" or y == "no" or y == "n":
            break
        else:
            print "Type a valid answer."

