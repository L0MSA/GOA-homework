# შემოვატანინოთ მომხმარებელს ციფრი
numbers = [float(input("Enter number {}: ".format(i + 1))) for i in range(5)]

# არითმეტიკული ოპერაციების დაწყება.
# შეკრება
addition_result = sum(numbers)

# გამოკლება
subtraction_result = numbers[0] - numbers[1] - numbers[2] - numbers[3] - numbers[4]

# გამრავლება
multiplication_result = numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4]

# გაყოფა
division_result = numbers[0] / numbers[1] / numbers[2] / numbers[3] / numbers[4]

# მოდულები
modulus_result = numbers[0] % numbers[1]

# დამრგვალება გაყოფით
floor_division_result = numbers[0] // numbers[1]

# დაბეჭდვა
print("Addition Result:", addition_result)
print("Subtraction Result:", subtraction_result)
print("Multiplication Result:", multiplication_result)
print("Division Result:", division_result)
print("Modulus Result:", modulus_result)
print("Floor Division Result:", floor_division_result)
