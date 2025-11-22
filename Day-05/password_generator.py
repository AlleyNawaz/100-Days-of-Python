import random

# Lists containing all possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# User input for password complexity
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


# EASY LEVEL (Not shuffled)
# password = ""

# # Add random letters
# for char in range(nr_letters):
#     password += random.choice(letters)

# # Add random numbers
# for char in range(nr_numbers):
#     password += random.choice(numbers)

# # Add random symbols
# for char in range(nr_symbols):
#     password += random.choice(symbols)

# print(password)


# HARD LEVEL (Shuffled password)

password_list = []   # Temporary list to store individual characters

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)     # Show before shuffle (optional)

# Shuffle the order of characters to make password stronger
random.shuffle(password_list)
print(password_list)     # Show after shuffle

# Combine list items into a final password string
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")