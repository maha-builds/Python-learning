hotel_room = {
    1: 1000,
    2: 2000,
    3: 3000
}

bookings = {}

while True:

    print("1. View Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. View Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available Rooms:")

        for room, price in hotel_room.items():
            if room not in bookings.values():
                print("Room", room, "- Price:", price)

    elif choice == "2":
        customer_name = input("Enter your name: ")
        bookedroom_number = int(input("Enter your room number: "))

        if bookedroom_number in hotel_room:

            if bookedroom_number not in bookings.values():
                bookings[customer_name] = bookedroom_number
                print("Room booked successfully")

                print("Customer name:", customer_name)
                print("Room number:", bookedroom_number)
                print("Room price:", hotel_room[bookedroom_number])

            else:
                print("Room is already booked")

        else:
            print("Room is not available")

    elif choice == "3":
        cancel_room = int(input("Enter your room number to cancel: "))

        found = False

        for name, room in list(bookings.items()):
            if room == cancel_room:
                del bookings[name]
                print("Booking cancelled")
                found = True
                break

        if not found:
            print("No booking found")

    elif choice == "4":
        if len(bookings) == 0:
            print("No booking found")
        else:
            print("Current Bookings:")

            for name, room in bookings.items():
                print("Customer name:", name)
                print("Room number:", room)
                print("Room price:", hotel_room[room])

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")
