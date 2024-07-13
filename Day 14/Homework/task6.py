int_list = [10, 5, 20, 15, 30]
sum_numbers = sum(int_list)
print("Sum of all numbers:", sum_numbers)

str_list = ["apple", "banana", "cherry", "apricot"]
total_length = sum(len(s) for s in str_list)
print("Total length of strings:", total_length)

game_results = [3, 1, 2, 0, 4]
total_score = sum(game_results)
print("Total score of the team:", total_score)

nested_lists = [[1, 2], [3, 4, 5], [6, 7]]
flattened_sum = sum(sum(sublist) for sublist in nested_lists)
print("Flattened sum of nested lists:", flattened_sum)
