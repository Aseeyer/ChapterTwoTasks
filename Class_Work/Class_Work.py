""" welcome to your new role at our fintech company! as part of your onboarding, you're tasked with developing a user-friendly mortgage calculator console application for our loan officers. This application will streamline the process of calculating monthly mortgage payments for our clients
here are the key features to consider:
principal: the amount the client wishes to borrow.
annual interest rate: The yearly interest rate offered on the mortgage. 
Duration: The duration of the mortgage in years.
The application should ask for these data and automatically calculate the monthly payment for the client 

tip: to get the percentage monthly rate, you divide the annual interest rate by percentage and number of months in a year and to get the number of months from the duration you multiply it  by number of months in a year. """


principal = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
annual_duration = int(input("Enter the duration of the loan: "))


PERCENTAGE = 100
MONTHS_IN_YEAR = 12
monthly_rate = float((annual_interest_rate/PERCENTAGE) / MONTHS_IN_YEAR)
monthly_duration = int(annual_duration * MONTHS_IN_YEAR)

monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** monthly_duration) / ((1 + monthly_rate) ** monthly_duration - 1)

print("The Monthly payment on a principal on #", principal ,"is" , monthly_payment)