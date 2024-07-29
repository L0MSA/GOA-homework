def extract_indices(lst):
    indices = [lst[1], lst[2], lst[3], lst[5]]
    return indices

elements = [10, 20, 30, 40, 50, 60, 70]
selected_indices = extract_indices(elements)
print("Selected indices:", selected_indices)
