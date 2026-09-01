Inventory = {}

for i in range(2):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    Inventory[product] = quantity

print(Inventory)

search_product = input("Enter product name: ")

if search_product in Inventory:
    print(Inventory[search_product])
else:
    print("Product not found")

remove_product = input("Enter product name: ")

if remove_product in Inventory:
    del Inventory[remove_product]
    print("Product removed")
else:
    print("Product not found")

while True:
    print("1. Add product")
    print("2. Remove product")
    print("3. Search products")
    print("4. Update products")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Add product")

    elif choice == 2:
        print("Remove product")

    elif choice == 3:
        print("Search products")

    elif choice == 4:
        print("Update products")

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice")
