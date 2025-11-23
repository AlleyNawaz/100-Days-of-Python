# Link to the Maze challenge world:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Function to turn right (Reeborg has no direct turn_right function)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until you hit a wall
while front_is_clear():
    move()
turn_left()  # Turn left to start solving the maze

# Maze-solving loop (right-hand rule)
while not at_goal():
    if right_is_clear():       # If there is space on the right
        turn_right()
        move()
    elif front_is_clear():     # If the front is clear, keep moving
        move()
    else:                      # If blocked, turn left
        turn_left()