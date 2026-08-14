contacts = {}

for i in range(3):
    name = input("enter contact name: ")
    phone_number = int(input("enter phone number: "))
    contacts[name] = phone_number

print(contacts)

search_name = input("Enter search name: ")

if search_name in contacts:
    print(contacts[search_name])
else:
    print("no such contact")
