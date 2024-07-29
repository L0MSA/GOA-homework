items_dict = {}

for i in range(1, 1001):
    key = f"item_{i}"
    value = i
    items_dict[key] = value

for key in list(items_dict.keys())[:10]:
    print(f"{key}: {items_dict[key]}")
