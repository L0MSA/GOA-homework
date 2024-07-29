def find_smallest_member(lst):
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest

numbers = [10, 5, 20, 15, 30]
smallest_number = find_smallest_member(numbers)
print("Smallest number:", smallest_number)
