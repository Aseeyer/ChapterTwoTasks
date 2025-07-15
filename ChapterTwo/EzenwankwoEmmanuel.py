#                     Exercise For Chapter Two

#                          Number 2.1

x = 2
y = 3

#for (a)
x = 2

#for (b)
#value of 2 + 2 is 4

# for (c)
# x = 

#for (d)
# 5 = 5

#                        Number 2.2

#The rating = input('Enter an integer rating between 1 and 10'). this returns a str instead of an int. So it should be

rating = int(input('Enter an integer rating between 1 and 10: '))

#                        Number 2.3
grade = 91
if grade >= 90:
    print ('Congratulations! Your grade of 91 earns you an A in this course')

#                        Number 2.4

print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)

#                        Number 2.5

radius = 2
pi = 3.14159

diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius * radius

print('The Diameter is: ', diameter)
print('The Circumference is: ', circumference)
print('Area is ', area)

#                       Number 2.6

number = int(input('Pick a number '))

if number % 2 == 0:
    print(number, 'is an even number')
else:
    print(number, 'is an odd number')

#                       Number 2.7

if 1024 % 4 == 0:
    print('1024 is a multiple of 4')
else:
    print('1024 is not a multiple of 4')

if 10 % 2 == 0:
    print('10 is a multiple of 2')
else:
    print('10 is not a multiple of 2')

#                       Number 2.8

print('number\tsquare/tcube')
print(0,'\t', 0**2,'\t', 0**3)
print(1,'\t', 1**2,'\t', 1**3)
print(2,'\t', 2**2,'\t', 2**3)
print(3,'\t', 3**2,'\t', 3**3)
print(4,'\t', 4**2,'\t', 4**3)
print(5,'\t', 5**2,'\t', 5**3)

#                       Number 2.9
print(ord('B'))
print(ord('C'))
print(ord('D'))
print(ord('b'))
print(ord('c'))
print(ord('d'))
print(ord('0'))
print(ord('1'))
print(ord('2'))
print(ord('5'))
print(ord('*'))
print(ord('+'))
#print(ord(' '))   

#                    Number 2.10

a = int(input('Enter first number '))
b = int(input('Enter second number '))
c = int(input('Enter third number '))

print('The sum is ', a + b + c)
print('The average is ', (a + b + c) / 3)
print('The product is ', a * b * c)
print('The Smallest is', min(a, b, c))
print('The Largest is ', max(a, b, c))

#                    Number 2.11

number = int(input("Enter a five-digit number: "))

digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit3 = (number % 1000) // 100
digit4 = (number % 100) // 10
digit5 = number % 10

print(digit1, digit2, digit3, digit4, digit5) 

#                    Number 2.12

# a = p(1 + r)^n
p = 1000
r = 0.07

# For 10, 20, 30 years
a10 = p * (1 + r) ** 10
a20 = p * (1 + r) ** 20
a30 = p * (1 + r) ** 30

print('After 10 years: $', a10)
print('After 20 years: $', a20)
print('After 30 years: $', a30)

#                    Number 2.13

Big_Python_Number = 1000 ** 1000
print(Big_Python_Number)

#                    Number 2.14

age = int(input("Enter your age: "))

max_heart_rate = 220 - age
lower_bound = max_heart_rate * 0.50
upper_bound = max_heart_rate * 0.85

print('Maximum heart rate is', max_heart_rate)
print('Target heart rate range is', lower_bound, 'to', upper_bound)

#                    Number 2.15

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

smallest = min(x, y, z)
largest = max(x, y, z)
middle = (x + y + z) - smallest - largest

print(smallest, middle, largest)



























