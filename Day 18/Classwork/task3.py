my_info = {
    "name": "Luka",
    "age": "16"
}

my_info.update({"email": "lomsa@gmail.com"})
my_info["surname"] = "Lomsadze"

print(my_info)

for value in my_info.values():
    print(value)
