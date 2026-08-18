inventory = {}

for i in range(3):
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[product] = quantity

print(inventory)

search_product = input("Enter search product: ")

if search_product in inventory:
    print(inventory[search_product])
else:
    print("Product not found")


product_name = input("Enter product name: ")
new_quantity = int(input("Enter new quantity: "))

if product_name in inventory:
    inventory[product_name] = new_quantity
    print("Updated inventory:", inventory)
else:
    print("Product not found")
