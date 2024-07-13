int_list = [10, 5, 20, 15, 30]
min_number = min(int_list)
print("Smallest number:", min_number)

str_list = ["apple", "banana", "cherry", "apricot"]
shortest_word = min(str_list, key=len)
print("Shortest word:", shortest_word)

temperature_list = [-5, 0, 10, -2, 3]
lowest_temperature = min(temperature_list)
print("Lowest temperature:", lowest_temperature)

products = [
    {"name": "Product A", "price": 20.5},
    {"name": "Product B", "price": 15.75},
    {"name": "Product C", "price": 30.0},
    {"name": "Product D", "price": 10.99}
]

min_price_product = min(products, key=lambda x: x['price'])
print("Product with minimum price:", min_price_product['name'], "- Price:", min_price_product['price'])
