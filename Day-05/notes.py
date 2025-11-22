# Day 5 => For Loops, Range and Code Blocks

# For Loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
    
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)
sum = 0
for score in student_scores:
    sum += score
    
print(sum)

# Range 
for number in range(1, 10):
    print(number)
# q till 9, 10 is not included

for number in range(1, 10, 3):
    print(number)
# Setp size

total = 0
for number in range(1, 101):
    total += number
print(total)