students={}
for i in range(4):
    name=input("Enter name: ")
    mark=int(input("Enter mark: "))
    students[name]=mark

    if mark>=50:
        print("Pass")

    else:
        print("Fail")
