def main():
    students=[]

    for i in range(4):
        student=input("Enter the student name: ")
        mark=int(input("Enter the mark: "))
        students.append({"name":student,"mark":mark})

        highest=students[0]
        for student in students:
            if student["mark"]>highest["mark"]:
                highest=student

    print("Highest mark:",highest["name"],highest["mark"])

main()
