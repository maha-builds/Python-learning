balance=5000
while True:
    try:
        withdraw_amount=int(input("Enter withdraw amount"))
        if balance<withdraw_amount:
            print("Insufficient balance")
        else:
            balance=balance-withdraw_amount
            print(f"Withdrawn! Remaining balance:{balance}")
            break
    except ValueError:
        print("Enter numbers only!")
