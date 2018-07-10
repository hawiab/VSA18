# Name:
# Date:

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

# sum = 0
# UserNo = raw_input("Enter a number to sum, or 0 to indicate you are finished: ")
#
# while int(UserNo) >= 0:
#     sum = sum + int(UserNo)
#     UserNo = raw_input("Enter a number to sum, or 0 to indicate you are finished: ")
#     if int(UserNo) == 0:
#         break
# print sum


# loop = 0
# x = 1
# sum = 0
#
# while loop < 5 and x != 0:
#     x = int(raw_input("Input a number or 0 when finished"))
#     loop = loop + 1
#     sum = sum + x
# print "The sum of your numbers is " + str( sum) + "!"

# FibNum = raw_input("How many Fibonacci numbers would you like to generate? ")
# CurrentNum = 1
# PreviousNum = 0
# num = "num"
# for num in range(int(FibNum)):
#     print CurrentNum
#     NextNum = int(CurrentNum) + int(PreviousNum)
#     PreviousNum = int(CurrentNum)
#     CurrentNum = int(NextNum)

FibNum = raw_input("How many Fibonacci numbers would you like to generate? ")
CurrentNum = 1
PreviousNum = 0