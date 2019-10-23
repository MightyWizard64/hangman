# Eric Nunez
# 10/21/19
# Period 6

import os
import time
import random 

frameList = [
'''
  +---+
      |
      |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
      |
      |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
  |   |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
  |\\ |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
      |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
 /    |
      |
    ===
'''
,
'''
  +---+
  O   |
 /|\\ |
  |   |
 / \\ |
      |
    ===
'''
]
secretWord = ["halloween","candy","costume","scare","monster"]
randomWord = random.choice(secretWord)

letterList = list(randomWord)
secret = []
misses = 0

print(frameList[misses])
print("Welcome to Hang Man!")

while True::
	for a in letterList:
		secret.append("_")
	print(secret)

	letter = input("Enter a letter: ")

	if letter in randomWord:
		print("That letter is in the word")
		print(frameList[misses])
	else:
		print("That letter is not in the word")
		misses += 1
		print(frameList[misses])

	secret[2] = letter



