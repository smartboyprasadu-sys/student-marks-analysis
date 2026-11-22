# Student Marks Analysis

marks = [85, 72, 90, 65, 30]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 35:
        passed += 1

pass_percentage = (passed / len(marks)) * 100

print("===== Student Marks Analysis =====")
print("All Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Students Passed:", passed)
print("Pass Percentage:", pass_percentage, "%")