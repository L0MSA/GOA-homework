int_list = [1, 5, 2, 5, 3, 5, 4, 5]
count_5 = int_list.count(5)
print("Number of times 5 appears:", count_5)

str_list = ["apple", "banana", "cherry", "apricot"]
count_a = sum(s.count('a') for s in str_list)
print("Number of times 'a' appears:", count_a)

bool_list = [True, False, True, True, False]
count_true = bool_list.count(True)
print("Number of True values:", count_true)

nested_list = [[1, 2], [3, 4], [3, 4], [5, 6]]
count_sublist = sum(1 for sublist in nested_list if sublist == [3, 4])
print("Number of occurrences of [3, 4]:", count_sublist)
