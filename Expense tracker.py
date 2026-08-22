expense = {}

expenses = int(input("Enter how many expenses: "))

for i in range(expenses):
    expense_name = input("Enter expense name: ")
    expense_amount = int(input("Enter expense amount: "))
    expense[expense_name] = expense_amount

print(expense)

total = sum(expense.values())
print("Total expenses:", total)

search_name = input("Enter search name: ")

if search_name in expense:
    print(expense[search_name])
else:
    print("Expense not found")

remove_name = input("Enter remove name: ")

if remove_name in expense:
    print(expense.pop(remove_name))
else:
    print("Expense not found")

print(expense)
