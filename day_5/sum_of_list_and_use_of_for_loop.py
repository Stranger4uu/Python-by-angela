students_score = [30,94,53,53,66,53,63,72,24,9,3,23,44,16,86,84,57,98,66,99,87,45,88,13,27,47]
sum_of_all_students_score = sum(students_score)
print(sum_of_all_students_score)

# Or

sum = 0
for scores in students_score:
    sum += scores

print(sum)

# to find largest number in the list we can use max function 

print(max(students_score))

#Or 

max_score = 0
for scores in students_score:
    if scores > max_score:
        max_score = scores

print(max_score)