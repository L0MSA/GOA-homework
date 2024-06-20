age = int(input("Enter your age: "))

if age > 5 and age < 12:
    print("You are a child.")
elif age >= 12 and age < 18:
    print("You are a teenager.")
elif age >= 18:
    print("You are an adult.")
else:
    print("Your age does not fit into any category.")
