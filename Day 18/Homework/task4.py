shopping_cart = {}

num_items = int(input("How many items do you want to buy? "))

for i in range(num_items):
    item = input(f"Enter the name of item {i + 1}: ")
    quantity = int(input(f"Enter the quantity of {item}: "))
    shopping_cart[item] = quantity

print("Your shopping cart contains:")
for item, quantity in shopping_cart.items():
    print(f"{quantity} x {item}")
