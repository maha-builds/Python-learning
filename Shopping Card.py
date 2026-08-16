cart = []

for i in range(3):
    product_name = input("Enter the product name: ")
    cart.append(product_name)

print("Cart:", cart)
print(len(cart))

remove_name = input("Enter the remove product: ")
cart.remove(remove_name)

search_product = input("Enter the product to search: ")

if search_product in cart:
    print("product found")
else:
    print("product not found")

print(cart)
