user_input = int(input("Input Number: "))

total_sum = 0

for number in range(1, user_input + 1):
    total_sum += number

print(f"{user_input}-მდე ყველა რიცხვის ჯამი არის: {total_sum}")
