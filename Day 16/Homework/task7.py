def remove_and_sum(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return sum(evens), sum(odds)

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
even_sum1, odd_sum1 = remove_and_sum(numbers1)
even_sum2, odd_sum2 = remove_and_sum(numbers2)
print("Even sums:", even_sum1, even_sum2)
print("Odd sums:", odd_sum1, odd_sum2)
