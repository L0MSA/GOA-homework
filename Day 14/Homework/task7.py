import random

random_integers = [random.randint(1, 100) for _ in range(10)]
length_random_integers = len(random_integers)
print("Length of list of random integers:", length_random_integers)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
num_weekdays = len(weekdays)
print("Number of weekdays:", num_weekdays)

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
nested_list_length = len(nested_list)
print("Length of nested list:", nested_list_length)

user_input = input("Enter a string: ")
string_length = len(user_input)
print("Length of the input string:", string_length)
