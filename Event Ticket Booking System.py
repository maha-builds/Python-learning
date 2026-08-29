available_seats=20

customer_name=input("enter customer name: ")
ticket_booking=int(input("enter ticket booking: "))

if ticket_booking<=available_seats:
    print("Booking allow")
    available_seats=available_seats-ticket_booking
    print("Booking successful!")
else:
    print("Not enough seats available")

ticket_price=200
total=ticket_booking*ticket_price
print("total_amount:",total)

print("Customer Name:",customer_name)
print("Number of tickets:",ticket_booking)
print("Remaining available seats:",available_seats)

cancel_ticket=int(input("enter cancel ticket count: "))
available_seats+=cancel_ticket
print("booking cancelled successfully!")

while True:
    print("\n===== EVENT TICKET BOOKING =====")
    print("1. booking ticket")
    print("2. canceling ticket")
    print("3. viewing available seats")
    print("4. exiting ticket")

    choice=int(input("enter choice: "))

    if choice==1:
        print("booking ticket")
    elif choice==2:
        print("canceling ticket")
    elif choice==3:
        print("viewing available seats:",available_seats)
    elif choice==4:
        print("thank you")
        break
    else:
        print("invalid choice")
