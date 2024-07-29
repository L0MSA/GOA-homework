def separate_odd_even(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens, odds

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
even_numbers1, odd_numbers1 = separate_odd_even(numbers1)
even_numbers2, odd_numbers2 = separate_odd_even(numbers2)
print("Even numbers:", even_numbers1, even_numbers2)
print("Odd numbers:", odd_numbers1, odd_numbers2)
