customer_name=input("Enter your name: ")
units=int(input("Enter units consumed: "))
if units<=100:
    total_bill=units*2
elif units<=200:
    total_bill=100*2+(units-100)*3
else:
    total_bill=100*2+100*3+(units-200)*5

print("Total bill:",total_bill)
