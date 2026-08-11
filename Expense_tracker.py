expense_amount1 = int(input("Enter the expense amount1: "))
expense_amount2 = int(input("Enter the expense amount2: "))
expense_amount3 = int(input("Enter the expense amount3: "))

total_expense = expense_amount1 + expense_amount2 + expense_amount3
print("Total Expense:", total_expense)

expense_category = input("Enter the expense category: ")
category_amount = int(input("Enter the expense category's amount: "))

budget = int(input("Enter the monthly budget: "))

if total_expense <= budget:
    status = "Within budget"
else:
    status = "Budget exceeded"

print("Status:", status)

print("Monthly budget:", budget)

Remaining = budget - total_expense
print("Remaining budget:", Remaining)

if category_amount <= total_expense:
    print("Category expense is valid")
else:
    print("Category is not valid")

expense_percentage = (total_expense / budget) * 100
print("Expense percentage:", expense_percentage, "%")
