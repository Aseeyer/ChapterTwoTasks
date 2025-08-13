#    NUMBER 3.1
passes = 0

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    if result != 1 and result != 2:
        print('Invalid input. Please enter 1 or 2.')
        result = int(input('Please Try Again!. Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1

failures = 10 - passes

print('Passed', passes)
print('Failed', failures)

if passes > 8:
    print('Bonus to instructor')
elif passes < 5:
    print('Try better next time')



#    NUMBER 3.2
a = b = 7
print('a',  a,'\nb =', b)
# The code looks very okay. i checked and it does work very fine


#    NUMBER 3.3
# Depending on the value of row, in each iteration, it prints >>>>>>>>>> or <<<<<<<<<< for a total of 10 times



#    NUMBER 3.4
for symbol in range(2):
    for symbols in range(7):
        print('@', end='')
    print()


#    NUMBER 3.5
print('Enter two integers, and i will tell you the relationship they satisfy')

number1 = int(input('Enter first interger: '))
number2 = int(input('Enter second interger: '))

if number1 == number2:
    print(number1, 'is equal to', number2)
elif number1 != number2:
    print(number1, 'is not equal to', number2)
if number1 < number2:
    print(number1, 'is less than', number2)
elif number1 > number2:
     print(number1, 'is greater than', number2)
if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
elif number1 >= number2:
    print(number1, 'is greater than or equal to', number2)



#    NUMBER 3.6
script1 = input('What is your problem? ')
script2 = input('Have you had this problem before (yes or no)? ')

if script2 == 'yes':
    print('Well, you have it again')
elif script2 == 'no':
    print('Well, you have it now')
#this does not show intelligent behaviour. the entity does not actually evaluate my initial input and simply runs unitellgently 



#    NUMBER 3.7
print(f'{"number":>6} {"square": >7} {"cube":>5}')
for number in range (6):
    square = number ** 2
    cube = number **3
    print(f'{number:>6} {square:>7} {cube:>5}')


#    NUMBER 3.8
numbers = [int(input(f'Enter number {i+1}: ')) for i in range(4)]

print('The sum is', sum(numbers))
print('The average is', sum(numbers) / 4)
print('The product is', numbers[0] * numbers[1] * numbers[2] * numbers[3])
print('The smallest is', min(numbers))
print('The largest is', max(numbers))


#    Number 3.9
number = int(input("Enter a five-digit number: "))
divisor = 10000
for i in range (5):
    digit = number // divisor
    print(digit, end='  ')
    number = number % divisor
    divisor = divisor // 10


#    NUMBER 3.10
p = 1000
r = 0.07

print(f'{"Year":<5} {"Amount":>10}')
for year in range(1, 31):
    amount = p * (1 + r) ** year
    print(f'{year:<5} ${amount:>10.2f}')


#    NUMBER 3.11
total_miles = 0
total_gallons = 0

while True:
    miles = float(input("Enter miles driven (-1 to quit): "))
    if miles == -1:
        break

    gallons = float(input("Enter gallons used: "))
    
    mpg = miles / gallons
    print(f"Miles per gallon for this tankful: {mpg:.2f}")

    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"\nOverall miles per gallon: {overall_mpg:.2f}")
else:
    print("\nNo data entered.")

#    NUMBER 3.12
number = int(input("Enter a five-digit number: "))

digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit3 = (number % 1000) // 100
digit4 = (number % 100) // 10
digit5 = number % 10

if digit1 == digit5 and digit2 == digit4:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

#    NUMBER 3.13

integer = int(input("Enter a non-negative integer: "))
factorial = 1
for number in range(1, integer + 1):
    factorial *= number
print(f"The factorial of {integer} is {factorial}")

#    NUMBER 3.14"""



#    NUMBER 3.15

factorial = 1
constant_e = 1
for number in range(1, 11):
    factorial *= number
    print
    constant_e += 1 / factorial
print("The estimated value is ", constant_e)


#    NUMBER 3.16

largest = 0
second_largest = 0

for num in range(10):
    number = int(input("Enter a number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)


#    NUMBER 3.17

# (a)
for i in range(1, 11):
    print('*' * i)
print()

# (b)
for i in range(10, 0, -1):
    print('*' * i)
print()

# (c)
for i in range(10, 0, -1):
    print(' ' * (10 - i) + '*' * i)
print()

# (d)
for i in range(1, 11):
    print(' ' * (10 - i) + '*' * i)


#    NUMBER 3.18

rows = 10

for i in range(1, rows + 1):
    # Pattern (a)
    print('*' * i + ' ' * (rows - i), end='   ')
    
    # Pattern (b)
    print('*' * (rows - i + 1) + ' ' * (i - 1), end='   ')
    
    # Pattern (c)
    print(' ' * (i - 1) + '*' * (rows - i + 1), end='   ')
    
    # Pattern (d)
    print(' ' * (rows - i) + '*' * i)

#    NUMBER 3.19

for side1 in range(1, 21):
    for side2 in range(1, 21):
        for hypotenuse in range(1, 21):
            if side1**2 + side2**2 == hypotenuse**2:
                print(side1, side2, hypotenuse)

#    NUMBER 3.20

binary = int(input("Enter a binary number: "))
decimal = 0
power = 0

while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** power)
    power += 1
    binary //= 10

print("Decimal:", decimal)


# NUMBER 3.21

price = float(input("Enter purchase price (<= 1 dollar): "))
change = int(round((1 - price) * 100))

quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
pennies = change % 5

print("Your change is:")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")


#    NUMBER 3.22

for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)
    if value == -1:
        break
else:
    print('The loop terminated without executing the break')

#    NUMBER 3.23

grade = 93
if grade >= 90:
  print('A')
  print('Great Job!')
  print('Take a break from studying')


#    NUMBER 3.24
#    NUMBER 3.25
#    NUMBER 3.26
#    NUMBER 3.27


#    NUMBER 3.28
#    NUMBER 3.29
#    NUMBER 3.30
#    NUMBER 3.31







































