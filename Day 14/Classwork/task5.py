def my_max(numbers):
    if not numbers:
        return None

    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

def my_min(numbers):
    if not numbers:
        return None

    min_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num

    return min_value

def my_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [4, 2, 8, 6, 1, 9]

print("Custom max function result:", my_max(numbers))

print("Custom min function result:", my_min(numbers))

print("Custom sum function result:", my_sum(numbers))
