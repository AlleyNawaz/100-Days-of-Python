# Day 7 => Hangman Project

"""
Your goal is to build a Hangman game using everything you have learned in Python.

Demo Final Project:
https://appbrewery.github.io/python-day7-demo/

The project is split into 5 major steps. Each step has multiple TODOs.
Your task is to complete each TODO in order.

TODO-1
Randomly choose a word from word_list and assign it to a variable called chosen_word. Then print it.

TODO-2
Ask the user to guess a letter. Store it in the variable guess and convert it to lowercase.

TODO-3
Loop through each letter in chosen_word.
If the guessed letter matches, print "Right".
If not, print "Wrong".
"""

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and convert it to lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

# TODO-3 - Check if the guessed letter is in chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")