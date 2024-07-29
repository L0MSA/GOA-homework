def find_largest_member(lst):
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return largest

numbers = [10, 5, 20, 15, 30]
largest_number = find_largest_member(numbers)
print("Largest number:", largest_number)
