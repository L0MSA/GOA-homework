names_list = []

for i in range(5):
    name = input(f"Enter name #{i + 1}: ")
    names_list.append(name)

selected_name = input("Enter the name you want to count: ")

name_count = names_list.count(selected_name)

print(f"The name '{selected_name}' is repeated {name_count} times in the list.")
