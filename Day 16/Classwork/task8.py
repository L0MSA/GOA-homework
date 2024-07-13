mixed_list = [10, "Hello", 20, "World", 30]
sum_integers = 0
concat_strings = ""
for item in mixed_list:
    if isinstance(item, int):
        sum_integers += item
    elif isinstance(item, str):
        concat_strings += item
print(sum_integers)
print(concat_strings)
