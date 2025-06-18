student_scores = [85, 90, 78, 92, 88]

# print(sum(student_scores))

sum = 0
for score in student_scores:
    sum += score
print(sum)

# print(max(student_scores))

max_score = 0
for maximum in student_scores:
    if maximum > max_score:
        max_score = maximum
print(max_score)