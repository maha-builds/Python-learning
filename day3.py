def student_average(tamil,english,maths):
    average=(tamil+english+maths)/3
    total=round(average,2)
    print("Student average marks:",total)
tamil=float(input("Enter tamil mark: "))
english=float(input("Enter english mark: "))
maths=float(input("Enter maths mark: "))
student_average(tamil,english,maths)
