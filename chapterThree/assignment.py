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














































