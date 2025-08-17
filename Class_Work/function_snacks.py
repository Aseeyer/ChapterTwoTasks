"""
1. create a function named divide_or_square that takes a number as input. If the number is divisible by 5, the function should return its square root. Otherwise, it should return the remainder of the number divided by 5. Handle potential edge cases like negative numbers and non-intergers input.
2. Write a function that takes investment_amount, monthly_interestRate, years as parameter and computes a future investment value at a given interest rate for a specified number of years. The future investment is determined using the formula      
future_investment_value = investment_amount * (1 + monthly_interest_rate) ** numberOfMonths
3. write a function called only_floats, whih takes two parameters a and b, and returns 2 if both arguments are floats, returns 1 if only one argument is a float, and returns 0 if neither argument is a float
"""

import math

def divide_or_square(number):
   pass
    if int(number) < 0:
        raise ValueError("Number cannot be negative")

    if not isinstance(number, int):
        raise ValueError("it must be a number")

    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5


def get_future_investment(investment_amount, monthly_interest_rate, years):
    if not float(investment_amount).is_integer():
        raise ValueError("Investment amount must be a whole number")

    if int(investment_amount) < 0:
        raise ValueError("cannot be negative")

    number_of_months = years * 12

    future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_of_months
    return future_investment_value


def only_floats(a, b):
    if a < 0 or b < 0:
        raise ValueError("Number cannot be negative")
        
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float):
        return 1
    elif isinstance(b, float):
        return 1
    else:
        return 0

   