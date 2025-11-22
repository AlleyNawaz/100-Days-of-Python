student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0

for score in student_scores:
    if max_score < score:
        max_score = score
print(f"Maximum score is {max_score}")

min_score = student_scores[0]  # start with the first value

for score in student_scores:
    if score < min_score:
        min_score = score

print(f"Minimum score is {min_score}")