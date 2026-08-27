available_slot = 5

vehicle = input("Enter vehicle number: ")
vehicle_type = input("Enter vehicle type (car/bike): ")

if vehicle_type == "car":
    fee = 50
elif vehicle_type == "bike":
    fee = 20
else:
    print("Invalid vehicle type")
    fee = 0

if available_slot > 0:
    print("Parking allow")
    available_slot -= 1
    print("Vehicle", vehicle, "parked successfully")
    print("Parking fee:", fee, "rupees")
    print("Available slots:", available_slot)

elif available_slot < 1:
    print("Parking full")
