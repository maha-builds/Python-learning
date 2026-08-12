prices = []
total = 0

for price in range(1, 6):
    price = int(input("Enter the price: "))
    prices.append(price)

for price in prices:
    total = total + price

print("Total:", total)
print("Maximum price:", max(prices))
print("Minimum price:", min(prices))

different = max(prices) - min(prices)
print("Difference:", different)

print("Number of expenses:", len(prices))

average = total / len(prices)
print("Average:", average)

search_price = int(input("Enter the price to search: "))

if search_price in prices:
    print("Price found")
else:
    print("Price not found")

prices.sort()
print("Sorted prices:", prices)

print("Count of 2:", prices.count(2))
