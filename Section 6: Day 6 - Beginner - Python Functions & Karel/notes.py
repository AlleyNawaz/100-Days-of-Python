# Day 6 => Functions, Code Blocks and While Loops

# Functions

def my_function():
    print("Hi there")

my_function()   # Calling the function


# Example 2: Function with parameter
def greet(name):
    print(f"Hello {name}")

greet("Ali")


# Example 3: Function that adds numbers
def add(a, b):
    print(a + b)

add(5, 7)


# For Loop

# for item in list_of_items:
#     Do something to each item

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# for number in range(a, b):
#     Prints numbers from a to b-1

for number in range(1, 5):
    print(number)   # Output: 1 2 3 4

# While Loop

# while something_is_true:
#     Do something repeatedly

count = 1
while count <= 5:
    print(count)
    count += 1   # Important: increase count to avoid infinite loop


# Infinite Loop Example (Don't run)

# while 5 > 3:
#     print("This will run forever")

# Robot Maze Example (From course)

# while at_goal != True:
# while not at_goal():
#     move_forward()
#     turn_left()

# (This is just a concept example, no real robot here)