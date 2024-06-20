while True:
    age = int(input("Please enter your age: "))
    
    if age >= 18:
        print("You are eligible to enter the program.")
        break
    else:
        print("Sorry, you cannot enter the program. You must be at least 18 years old.")
