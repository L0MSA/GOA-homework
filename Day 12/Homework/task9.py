budget = float(input("Enter your budget: "))

item_price = float(input("Enter the price of the item you want to buy: "))

if budget >= item_price:
    print("You can buy the item.")
else:
    print("Sorry, you cannot buy the item.")
