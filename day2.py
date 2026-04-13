def petrol_cost(petrol):
    price=102.72
    petrol_cost=petrol*price
    cost= round(petrol_cost,2)
    print("Petrol_cost:" ,cost)
petrol=int(input("Enter how many liter fill: "))
petrol_cost(petrol)
