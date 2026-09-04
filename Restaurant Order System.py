menu = {
    "dosa": 50,
    "burger": 50,
    "chicken": 50
}

total = 0

print("Menu:")
print("1. dosa")
print("2. burger")
print("3. chicken")
print("4. exit")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        quantity = int(input("Enter how many dosa you have order: "))
        total = total + quantity * menu["dosa"]
        print("Dosa total is:", quantity * menu["dosa"])

    elif choice == "2":
        quantity = int(input("Enter how many burger you have order: "))
        total = total + quantity * menu["burger"]
        print("Burger total is:", quantity * menu["burger"])

    elif choice == "3":
        quantity = int(input("Enter how many chicken you have order: "))
        total = total + quantity * menu["chicken"]
        print("Chicken total is:", quantity * menu["chicken"])

    elif choice == "4":
        break

    else:
        print("Sorry, you have no choice")

print("Total bill:", total)
