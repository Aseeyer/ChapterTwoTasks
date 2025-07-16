"""write a python program that calculates the number of liters of fuel a customer can purchase from a gas station, given their total budget. Assume the price per liter is #855
"""

user_amount = int(input("Enter how much you have: "))
PRICE_PER_LITER = 855

total_liters = user_amount / PRICE_PER_LITER
print("With #", user_amount, "you can buy ", total_liters,"liters")