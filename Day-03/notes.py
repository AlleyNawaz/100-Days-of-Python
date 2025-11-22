# Day 3 => Conditional Statements, Logical Operators, Code Blocks and Scope

# Modulo Operator % 
# Example: 10 / 5 = 2, but 10 % 5 = 0 (remainder after division)

# Even Number: 12 % 2 = 0 because even numbers divide cleanly with no remainder
numberToCheck = int(input("What number do you want to check? "))
if numberToCheck % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Task:
'''
BMI Calculator with interpretations.

If BMI is less than 18.5: print "underweight".
If BMI is between 18.5 and 25: print "normal weight".
If BMI is 25 or more: print "overweight".
'''

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")


# Rollercoaster Program
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wantsPhoto = input("Do you want a photo taken? Type y for Yes or n for No: ")

    if wantsPhoto == 'y':
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you need to be taller before you can ride.")


# Logical Operators: AND, OR, NOT
a = 12

a > 10 and a < 20   # True
a > 10 or a < 10    # True
not a < 0           # True (because a < 0 is False, and 'not' flips it)
not False           # True
not True            # False


# Both lines below do the same thing (clean range checking)
elif a >= 5 and a <= 12:
    print(a)

elif 5 <= a <= 12:
    print(a)