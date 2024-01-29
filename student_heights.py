student_heights = ["151", "145", "179", "165"]

total_height = 0
for height in student_heights:
    total_height += int(height)
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = 0
for mean in student_heights:
    average_height = (total_height / number_of_students)
print(f"average height = {average_height}")
