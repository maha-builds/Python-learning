marks = {}

for i in range(3):
    student_name = input("Enter the student name: ")
    student_mark = int(input("Enter the student number: "))
    marks[student_name] = student_mark

highest_mark = max(marks.values())
print("Highest mark:", highest_mark)

for name, mark in marks.items():
    if mark == highest_mark:
        print(name)

print("Student name:", student_name)
print("Student mark:", student_mark)

search_name = input("Enter the search name: ")

if search_name in marks:
    print(marks[search_name])
else:
    print("student not found")
