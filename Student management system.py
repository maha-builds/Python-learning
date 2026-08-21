students = {}

name = input("Enter student name: ")
mark = int(input("Enter mark: "))
students[name] = mark

print(students)

student_name = input("Enter student name: ")

if student_name in students:
    print(students[student_name])
else:
    print("Student not found")

new_student = input("Enter new student name: ")
new_student_mark = int(input("Enter new student mark: "))
students[new_student] = new_student_mark

remove_name = input("Enter remove student name: ")

if remove_name in students:
    del students[remove_name]
else:
    print("Student not found")

print(len(students))


print
