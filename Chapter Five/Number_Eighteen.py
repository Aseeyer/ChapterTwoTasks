# Summing the Triples of the Even Integers from 2 through 10



numbers = list(range(1, 11))



total = sum(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, numbers)))

print("Sum using filter & map:", total)



total2 = sum([x * 3 for x in numbers if x % 2 == 0])

print("Sum using list comprehension:", total2)