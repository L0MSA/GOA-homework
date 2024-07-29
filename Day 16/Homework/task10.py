def collect_ints_concat_strings(*lists):
    integers = []
    strings = []
    for lst in lists:
        for item in lst:
            if isinstance(item, int):
                integers.append(item)
            elif isinstance(item, str):
                strings.append(item)
    return integers, ''.join(strings)

list1 = [1, 2, "apple", 3]
list2 = ["banana", 4, "cherry", 5]
ints, concatenated_strs = collect_ints_concat_strings(list1, list2)
print("Integers:", ints)
print("Concatenated strings:", concatenated_strs)
