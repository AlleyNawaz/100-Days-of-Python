"""
TODO-1
Create an empty string called placeholder.
For each letter in chosen_word, add "_" to placeholder.
So if chosen_word = "apple", then placeholder should be "_____" (5 blanks).
Print the placeholder as a hint.

TODO-2
Create an empty string called display.
Loop through chosen_word.  
If the letter matches the user's guess, add that letter to display.
If not, add "_".
Example:
guess = "p" and chosen_word = "apple"
display should become "_pp__"
Then print display.
"""

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)  # Only for testing/hint

# TODO-1: Create a placeholder with "_" for each letter in chosen_word
placeholder = ""
word_length = len(chosen_word)

for _ in range(word_length):
    placeholder += "_"

print(placeholder)

# Take user guess
guess = input("Guess a letter: ").lower()

# TODO-2: Build "display" with guessed letters revealed
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)