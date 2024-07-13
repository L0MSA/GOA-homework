int_list = [10, 5, 20, 15, 30]
max_number = max(int_list)
print("Maximum number:", max_number)

str_list = ["apple", "banana", "cherry", "apricot"]
max_length = max(len(s) for s in str_list)
print("Maximum string length:", max_length)

age_list = [25, 30, 40, 50, 35]
oldest_age = max(age_list)
print("Oldest person's age:", oldest_age)

from datetime import datetime

date_list = [
    datetime(2023, 6, 1),
    datetime(2023, 7, 15),
    datetime(2023, 5, 10)
]

most_recent_date = max(date_list)
print("Most recent date:", most_recent_date)
