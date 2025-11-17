print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))

# Convert the tip percentage into a decimal
tipAsPercentage = tip / 100

# Calculate the total tip amount
totalTipAmount = bill * tipAsPercentage

# Add tip to the original bill
totalBill = bill + totalTipAmount

# Split the bill among the people
billPerPerson = totalBill / people

# Round the final amount to 2 decimal places
finalAmount = round(billPerPerson, 2)

print(f"Each person should pay: ${finalAmount}")