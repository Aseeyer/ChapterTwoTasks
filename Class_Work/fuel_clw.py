<<<<<<< HEAD
"""write a python program that calculates the number of liters of fuel a customer can purchase from a gas station, given their total budget. Assume the price per liter is #855


user_amount = int(input("Enter how much you have: "))
PRICE_PER_LITER = 855

total_liters = user_amount / PRICE_PER_LITER
print("With #", user_amount, "you can buy ", round(total_liters, 2),"liters")"""


age = input("Enter Your Age: ")

if age.isdigit():
    age = int(age)
    if age >= 18 and age <= 60:
        print("You are eligible to vote.")
    elif age < 18:
        print("You are too young to vote.")
    elif age > 60:
        print("You are too old.")
else:
    print("Who goes you! That's not a valid number.")
=======
"""write a python program that calculates the number of liters of fuel a customer can purchase from a gas station, given their total budget. Assume the price per liter is #855
"""

user_amount = int(input("Enter how much you have: "))
PRICE_PER_LITER = 855

total_liters = user_amount / PRICE_PER_LITER
print("With #", user_amount, "you can buy ", total_liters,"liters")
>>>>>>> 42ac0079e5af9d0f6a446b36d860ffb197c986c9
