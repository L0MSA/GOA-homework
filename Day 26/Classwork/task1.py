def filter_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    
    return even_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter_even_numbers(input_list)
print(even_list)
