total_sum = 0
total_product = 1
count = 0
max_number = 0
min_number = 100

for number in range(101):
    total_sum += number
    if number != 0:
        total_product *= number 
    count += 1
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

average = total_sum / count