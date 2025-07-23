for number in range(51):
    if number % 2 == 0:
        print(number ** 3, end=',')
   
    elif number % 2 != 0:
        print(number ** 2, end=',')