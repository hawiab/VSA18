import random
# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""





#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

# Part 1
# for item in a:
#     if item < 5:
#         print item
# # Extension

# list = []
# for item in a:
#     if item < 5:
#         list.append(item)
# print(list)





# Extension
# for item in a:
#     UserNum = raw_input("Choose a number: ")
#     if item < int(UserNum):
#         print item



#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# newlist = []
# for item in b:
#     if item == item in c:
#         newlist.append(item)
# print(newlist)

# list = []
# for item in range(10):
#     RandomNum = random.randint(1, 9)
#     list.append(RandomNum)
# print list
#
# list2 = []
# for item in range(10):
#     RandomNum = random.randint(1,9)
#     list2.append(RandomNum)
# print list2
#
# similarlist = []
# for item in list:
#     if item == item in list2:
#         similarlist.append(item)
# print similarlist


#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all 'a' with '*'.

# counter = 0
# for item in d:
#     if item == "a":
#         d[counter] = "*"
#     counter = counter + 1
# print d

#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

# UserWord = raw_input("Enter a word: ")
# UserWord = UserWord[0:].lower()
# UserList = []
#
# for letter in UserWord:
#     UserList.append(letter)
# while 0 == 0:
#     if UserList[0] == UserList[-1]:
#         UserList = UserList[1:-1]
#         print UserWord, "is a palindrome."
#     else:
#         print UserWord, "is not a palindrome."

Cards = [1,2,3,4,5,6,7,8,9,1,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
ShuffleDeck = []
for Card in Cards:
    RandomNum = random.randint(1, 52)
    if RandomNum != ShuffleDeck:
        ShuffleDeck.append(RandomNum)
        Cards.remove(RandomNum)
print ShuffleDeck



