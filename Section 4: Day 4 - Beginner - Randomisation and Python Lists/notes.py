# Day 4 => Randomisation and Python Lists

# Randomisation
import random
import my_module

# randint(a, b) gives a random integer between a and b (both included)
random_integer = random.randint(1, 10)
print(random_integer)

# Value coming from your custom module
print(my_module.my_fav_num)

# random.random() returns a number between 0.0 and 1.0 (1.0 not included)
random_number_0_to_1 = random.random() * 10   # This makes it between 0 and 10
print(random_number_0_to_1)

# random.uniform(a, b) gives a random float between a and b (both included)
random_float = random.uniform(1, 10)
print(random_float)

# Heads or Tails
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("heads")
else:
    print("tails")


# Lists => A data structure used to store multiple items
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
    "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
    "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
    "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
    "Hawaii"
]

print(states_of_america[0])   # First item
print(states_of_america[-1])  # Last item

print(states_of_america[1])
states_of_america[1] = "Pennsylvania"   # Correct spelling
print(states_of_america[1])

# Append adds a single item at the end
states_of_america.append("Islamabad")

# Extend adds multiple items at the end
states_of_america.extend(["Rawalpindi", "Jhelum", "Gujrat"])
print(states_of_america)

states_of_america.remove("Islamabad")
states_of_america.remove("Rawalpindi")
states_of_america.remove("Jhelum")
states_of_america.remove("Gujrat")

print(states_of_america)


# Nested Lists => A list inside another list
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)


fresh_fruits = ["Strawberries", "Nectarines", "Apples", "Grapes",
                "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fresh_fruits, vegetables]

# Accessing nested list: [list_index][item_index]
print(dirty_dozen[1][1])   # "Kale"