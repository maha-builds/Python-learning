Grocery=[
    {"item":"rice","price":300},
    {"item":"oil","price":150},
    {"item":"egg","price":40}
    ]
search=input("Enter item: ")
found=False

for g in Grocery:
    if g["item"]==search:
        print("Price:",g["price"])
        found=True
        break
    if found==False:
        print("Not Found!")
