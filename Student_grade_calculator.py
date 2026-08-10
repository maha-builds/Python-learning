student_name = input("Enter your name: ")
python = int(input("Enter your python mark: "))
java = int(input("Enter your java mark: "))
DS = int(input("Enter your DS mark: "))

total = python + java + DS
average = total // 3

if total >= 290:
    print("A grade")
elif total >= 200:
    print("B grade")
else:
    print("C grade")

print("Total:", total)
print("Average:", average)
