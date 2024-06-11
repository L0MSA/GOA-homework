"""მომხარებელს შემოატანინეთ თავისი ბიუჯეტი და შეამოწმეთ არის თუ არა მისი 
ბიუჯეტი 50 ლარზე მეტი ან 100 ლარზე მეტი"""
budget = float(input("Enter your budget in GEL: "))

if budget > 100:
    print("Your budget is more than 100 GEL.")
elif budget > 50:
    print("Your budget is more than 50 GEL but less than or equal to 100 GEL.")
else:
    print("Your budget is not more than 50 GEL.")
