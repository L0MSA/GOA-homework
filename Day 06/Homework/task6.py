"""დაწერეთ პროგრამა სადაც მომხმარებელს შემოატანინებთ ინფორმაციას თავის თავზე 
(name,surname,age,address,gmail) და შემდეგ დაუპრინტეთ ეს ინფორმაცია ერთ დიდ წინადადებად"""


name = input("Enter your name: ")

surname = input("Enter your surname: ")

age = input("Enter your age: ")

address = input("Enter your address: ")

gmail = input("Enter your Gmail: ")

welcome = (
f"My name is {name} {surname}, I am {age} year old. "

f"I live at {address}, my Gmail is {gmail}."
)

print(welcome)