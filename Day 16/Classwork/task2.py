original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
half_list = original_list[:len(original_list)//2]
new_list = []
new_list.extend(half_list)
print(new_list)
