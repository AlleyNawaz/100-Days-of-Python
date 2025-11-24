"""
TODO-1
Use a while loop to let the user guess multiple times.
The loop should stop only when the user has guessed all letters in chosen_word.
Once display has no more "_", the user wins.

TODO-2
Update the for loop so that previous correct guesses stay in the display string.
Currently, each new guess overwrites previous correct guesses.
"""

import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)
print(chosen_word)  # For testing purposes

# Create placeholder for chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: Use a while loop to let the user guess repeatedly
game_over = False
correct_letters = []  # Keep track of all correctly guessed letters

while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Update display to keep previous correct letters
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Check if all letters have been guessed
    if "_" not in display:
        game_over = True
        print("You win!")