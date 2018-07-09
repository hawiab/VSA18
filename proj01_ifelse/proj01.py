# Name: Hawi Abraham
# Date: 07/09/18

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.

# Variables
UserName = raw_input("Hello. What is your name? ")
UserGrade = raw_input("What grade are you in? ")

# This line makes the first letter uppercase and the remaining letters lowercase.
UserName = UserName[0].upper() + UserName[1:].lower()

# This function calculates how many years until you graduate
print UserName, "! You will graduate in", 12 - int(UserGrade), "years"

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday

# Current month and day variables
CurrentMonth = 7
CurrentDay = 9

# User variables
UserBirthMo = raw_input("Hello. When is your birth month? ")
UserBirthDay = raw_input("Hello. When is your day of birth?")


if int(UserBirthMo) <= CurrentMonth:
    if int(UserBirthDay) <= CurrentDay:
        print 12-(CurrentMonth - int(UserBirthMo)), "months and", 30 - (CurrentDay - int(UserBirthDay)), "days."
    else:
        print 12-(CurrentMonth - int(UserBirthMo)), "months and", int(UserBirthDay) - CurrentDay, "days."
elif int(UserBirthMo) == CurrentMonth and int(UserBirthDay) == CurrentDay:
    print 0, "months and", 0, "days."
else:
    if UserBirthDay <= CurrentDay:
        print int(UserBirthMo) - CurrentMonth, "months and", 30 - (CurrentDay - int(UserBirthDay)), "days."

    else:
        print int(UserBirthMo)-CurrentMonth, "months and", int(UserBirthDay) - CurrentDay, "days."

# User variable
UserAge = raw_input("Hello. How old are you? ")

if int(UserAge) >= 13 and int(UserAge) < 17:
    print "You are allowed to see G, PG, or PG-13-rated movies."
elif int(UserAge) < 13:
    print "You are allowed to see G and PG-rated movies."
else:
    print("You are allowed to see G, PG, PG-13, and R-Rated movies.")

# If you complete extensions, describe your extensions here!
