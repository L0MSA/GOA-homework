start_number = int(input("First Number: "))
end_number = int(input("Second Number: "))

total_sum = 0
total_product = 1

if start_number > end_number:
    start_number, end_number = end_number, start_number

for number in range(start_number, end_number + 1):
    total_sum += number
    total_product *= number

print(f"{start_number}-from {end_number}-to Sum is: {total_sum}")
print(f"{start_number}-from {end_number}-to Multi is: {total_product}")
