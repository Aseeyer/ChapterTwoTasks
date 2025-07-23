a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
smallest = a

if b > a and b > c:
    print("b is largest")
elif c > b and c > a:
    print("c is largest")
else:
    print("a is largest")


if b < a and b < c:
    print("b is smallest")
elif c < b and c < a:
    print("c is smallest")
else:
    print("a is smallest")



#number two
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

largest = number1
second_largest = 0

if number2 < largest and number2 > second_largest:
    print("Number2 is second largest")
elif number3 < largest and number3 > second_largest:
    print("Number3 is the second largest")
else:
    print("Number1 is the second largest")


#Number three

n = int(input("Enter a number between 1 and 7"))

if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednessday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n ==  7:
    print("Sunday")



word = 'Kingdom'

for letter in word:
    print(letter, end=',')

#for i in range()
#for letter in word:
#    if letter == 'd';
#    break
#print(number)

#for number in range (100)
#    if number == 10P
#   break
#print(number, end='')