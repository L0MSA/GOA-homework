correct_password = "password123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter the password: ")
    
    if entered_password == correct_password:
        print("Authorization successful! You have passed the authorization.")
        break
    else:
        print("Incorrect password. Please try again.")
