Ticket_booking = {}

for i in range(3):
    movie = input("Enter movie name: ")
    price = int(input("Enter ticket price: "))
    Ticket_booking[movie] = price

print(Ticket_booking)

chose_movie = input("Enter what movie you want: ")

if chose_movie in Ticket_booking:
    print(Ticket_booking[chose_movie])
else:
    print("Movie not found")

ticket = int(input("Enter how many tickets: "))

total = ticket * Ticket_booking[chose_movie]

print("Total amount:", total)
