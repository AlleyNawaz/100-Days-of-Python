# This method of taking out a specific character from a string is called subscripting.
# The number inside the square brackets tells which character you want to access.
# Subscripting example:
print("Hello"[0]) 

# We can also count backwards by using negative indexes, starting from the last character.
print("Hello"[-1]) 

# String concatenation:
print("123" + "345") 
# The + sign joins strings together.

# Integers = Whole numbers
print(123 + 345)

# Large integers:
print(123_456_789)
# This works the same as writing 123,456,789 (underscore improves readability).

# Float = Number with decimal values
print(3.14159)

# Boolean values:
print(True)
print(False)

# len(12345) → The len() function does NOT work on integers, only on sequences like strings.
print(len("Hello"))

# Checking data types:
print(type("Hello"))
print(type(123))
print(type(12.345))
print(type(True))

# Type conversion:
print(int("123") + int("345")) 

# Make this line run without errors:
# print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Mathematical operations:
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3)   # Output: 2.0 (Float) => Automatic type casting
print(6 // 3)  # Output: 2 (Integer)

print(5 / 3)   # Output: 1.666...
print(5 // 3)  # Output: 1 (Removes decimal part)

print(2**3)  # Exponent operator (**): raises a number to a power

# PEMDAS (Order of Operations): 
# Parentheses (), Exponents **, Multiplication/Division * or /, Addition/Subtraction + or -
# Python evaluates expressions from left to right within the same priority level.

print(3 * 3 + 3 / 3 - 3)      # Output: 7.0
print(3 * (3 + 3) / 3 - 3)    # Output: 7.0

# Task:
# BMI Calculator
# BMI (Body Mass Index) is a medical measure used to check if a person is underweight, healthy weight, overweight, or obese.
# Formula: BMI = weight (kg) / height² (m²)

height = 1.65   # height in meters
weight = 84     # weight in kilograms

bmi = weight / (height * height)

print(bmi)

# Number Manipulation and F-Strings

# Convert BMI to an integer (removes the decimal part)
print(int(bmi))

# Round BMI to the nearest whole number
print(round(bmi))

# Round BMI to 2 decimal places
print(round(bmi, 2))


# Assignment Operator (used to update a variable with its own value)
score = 0
score += 1   # Same as score = score + 1
print(score)


# F-Strings
totalScore = 100
height = 1.8
isWinning = True

# We have an integer, a float, and a boolean, and we want to combine them
# into one string using an f-string.
print(f"Total score = {score}, your height is {height}. You are winning is {isWinning}")