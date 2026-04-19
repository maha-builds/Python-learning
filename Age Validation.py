while True:
    try:
        age=int(input("Enter age: "))
        if age<0:
            print("Age cannot be negative")
        elif age>150:
            print("Invalid age")
        else:
            print(f"Your age is{age}")
            break

    except ValueError:
        print("Please enter a number")
