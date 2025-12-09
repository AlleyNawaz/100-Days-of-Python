# AND Operator Examples
# Example 1: Age and Height Check
age = 15
height = 130

if age >= 10 and height >= 120:
    print("You can ride the rollercoaster")
else:
    print("You cannot ride")
# You must be 10 or older AND 120cm or taller. Both must be True.

# Example 2: Login Check
username = "ali"
password = "1234"

if username == "ali" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
# Both conditions match → login works.


# OR Operator Examples
# Example 1: Free Entry for Kids or Seniors
age = 6

if age < 7 or age > 60:
    print("Entry is free")
else:
    print("You must buy a ticket")
# Only one condition must be True.

# Example 2: Discount Offer
isStudent = True
isMember = False

if isStudent or isMember:
    print("You get a discount")
else:
    print("No discount available")
# Student OR member → gets discount.


# NOT Operator Examples
# Example 1: Not Rain
isRaining = False

if not isRaining:
    print("You can go outside")
else:
    print("Take an umbrella")
# not False → True.

# Example 2: Checking No Access
isBanned = True

if not isBanned:
    print("You can enter")
else:
    print("Access denied")
    

# Combined Logical Operators
# Example: Movie Permission
age = 16
withParent = True

if age >= 18 or (age >= 13 and withParent):
    print("You can watch the movie")
else:
    print("You cannot watch")
# Either 18+ OR 13–17 with parent.

# Example: Strong Password
password = "Abc123"

if len(password) >= 6 and ("1" in password or "2" in password):
    print("Password is strong")
else:
    print("Password is weak")