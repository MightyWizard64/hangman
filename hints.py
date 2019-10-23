# Hints for Hang Man Project

# How to guess a word
myWord == "hello"

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match!")
else:
	print("It's not a match")
# how to check if a letter is in a word
letter = input("Type a letter: ")
if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter is not in the word")
# How to check where the letter is in the word
count = 0
##########
# how to turn a string into a list?
myString = "arizona"
myList = list(myString)
print(myList)
secret = []
# How to create a list with _ in place of letters?
for a in myList:
	secret.append("_")

print(secret)

# how to replace an _ with a letter

secret[2] = "i"
