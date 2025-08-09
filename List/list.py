class ArrayKata:

    def maximum_in_array(numbers):
        largest = numbers[0]
	for number in range(1, len(numbers)):
	    if numbers[i] > largest:
		largest = numbers[i]   

    def minimum_in_array(numbers):
        smallest = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < smallest:
                smallest = numbers[i]
        return smallest

    def sum_of(numbers):
        sum_of_array = 0
        for number in numbers:
            sum_of_array += number
        return sum_of_array

    def sum_of_even_numbers_in(numbers):
        sum_of_even_number = 0
        for number in numbers:
            if number % 2 == 0:
                sum_of_even_number += number
        return sum_of_even_number

    def sum_of_odd_numbers_in(numbers):
        sum_of_odd = 0
        for number in numbers:
            if number % 2 != 0:
                sum_of_odd += number
        return sum_of_odd

    def maximum_and_minimum_of(numbers):
        largest = numbers[0]
        smallest = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] > largest:
                largest = numbers[i]
            if numbers[i] < smallest:
                smallest = numbers[i]
        return [largest, smallest]

    def even_numbers_in(numbers):
        even_numbers = []
        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(number)
        return even_numbers

    def odd_numbers_in(numbers):
        odd_numbers = []
        for number in numbers:
            if number % 2 != 0:
                odd_numbers.append(number)
        return odd_numbers

    def number_of_even_numbers_in(numbers):
        count = 0
        for number in numbers:
            if number % 2 == 0:
                count += 1
        return count

    def number_of_odd_numbers_in(numbers):
        count = 0
        for number in numbers:
            if number % 2 != 0:
                count += 1
        return count

    def number_of_negative_numbers_in(numbers):
        count = 0
        for number in numbers:
            if number < 0:
                count += 1
        return count
