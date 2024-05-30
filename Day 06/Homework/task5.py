"""დაწერეთ პროგრამა სადაც შემოიტანთ თქვენი ოჯახის წევრების ასაკებს 
თქვენი დავალება იქნება რომ დაპრინტოთ რამდენი წლისები იქნებიან 20 წლის შემდეგ"""

moms = int(input("Enter your mom's age: "))

dads = int(input("Enter your dad's age: "))

grandpas = int(input("Enter your grandpa's age: "))

grandmas = int(input("Enter your grandma's age: "))

moms_age_in_20_years = moms + 20

dads_age_in_20_years = dads + 20

grandpas_age_in_20_years = grandpas + 20

grandmas_age_in_20_years = grandmas + 20


print(f"In 20 years, mom will be {moms_age_in_20_years} years old.")
print(f"In 20 years, dad will be {dads_age_in_20_years} years old.")
print(f"In 20 years, grandpa will be {grandpas_age_in_20_years} years old.")
print(f"In 20 years, grandma will be {grandmas_age_in_20_years} years old.")


