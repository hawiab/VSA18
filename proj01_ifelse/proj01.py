# Name: Hawi Abraham
# Date: 07/09/18

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.

# UserName = raw_input("Hello. What is your name? ")
# UserGrade = raw_input("What grade are you in? ")
# UserName = UserName[0].upper() + UserName[1:].lower()
# print UserName, "! You will graduate in", 12 - int(UserGrade), "years"
# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


CurrentMonth = 7
CurrentDay = 9
UserBirthMo = raw_input("Hello. When is your birth month? ")
UserBirthDay = raw_input("Hello. When is your day of birth?")
if int(UserBirthMo) < CurrentMonth
    if int(UserBirthDay) < CurrentDay
        print 12-(CurrentMonth - int(UserBirthMo)), "months and", 30 - (CurrentDay - int(UserBirthDay)), "days."
    else int(UserBirthDay) > CurrentDay
        print 12-(CurrentMonth - int(UserBirthMo)), "months and", int(UserBirthDay) - CurrentDay, "days."
else int(UserBirthMo) > 7
    if UserBirthDay < CurrentDay
    print int(UserBirthMo) - CurrentMonth, "months and", 30 - (CurrentDay - int(UserBirthDay)), "days."
    else UserBirthDay > CurrentDay
    print int(UserBirthMo)-CurrentMonth, "months and", int(UserBirthDay) - CurrentDay, "days."

# If you complete extensions, describe your extensions here!
