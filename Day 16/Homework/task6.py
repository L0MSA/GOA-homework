def separate_int_str(lst):
    int_list = [x for x in lst if isinstance(x, int)]
    str_list = [x for x in lst if isinstance(x, str)]
    return int_list, str_list

mixed_list = [1, "apple", 2, "banana", 3, "cherry"]
ints, strings = separate_int_str(mixed_list)
print("Integers:", ints)
print("Strings:", strings)
