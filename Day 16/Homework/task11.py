def move_even_indices(lst):
    new_list = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    return new_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = move_even_indices(original_list)
print("New list with elements at even indices:", new_list)
