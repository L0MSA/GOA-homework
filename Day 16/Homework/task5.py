def combine_lists(int_list, str_list):
    combined_list = []
    min_len = min(len(int_list), len(str_list))
    for i in range(min_len):
        combined_list.append(str_list[i])
        combined_list.append(int_list[i])
    return combined_list

integers = [1, 2, 3]
strings = ["a", "b", "c", "d"]
combined = combine_lists(integers, strings)
print("Combined list:", combined)
