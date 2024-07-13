list1 = [10, 20, 30, 40, 50]
list2 = [15, 25, 35, 45, 55]
min_list1 = min(list1)
max_list1 = max(list1)
min_list2 = min(list2)
max_list2 = max(list2)
result = max(max_list1, max_list2) - min(min_list1, min_list2)
result_list = [result]
print(result_list)
