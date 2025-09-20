#Creating the list with all True values
primes = [True] * 1000

#Setting 0 and 1 to False (not prime)
primes[0] = primes[1] = False

#Finding primes using the sieve
for index in range(2, int(1000**0.5) + 1):
    if primes[index]:
        for multiple in range(index*index, 1000, index):
            primes[multiple] = False

#Displaying all prime numbers
for number in range(1000):
    if primes[number]:
        print(number, end=" ")
