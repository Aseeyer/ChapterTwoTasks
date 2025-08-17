from functools import reduce


#SECTION ONE
#Number one
numbers = (1, 2, 3, 4)
next_number = 5

new_numbers = numbers + (next_number,)
print(numbers)
print(new_numbers)

#Number two
numbers =  (1, 2, [3, 4], 5)
numbers[2][1] = 99
print(numbers)

#Number three
fruits = ('apple', 'banana', 'cherry')
fruit_to_list = list(fruits)
print(fruit_to_list)
fruit_list_to_tuple = tuple(fruit_to_list)
print(fruit_list_to_tuple)

#Number four

numbers = (10, 20, 30, 40)
a, b, *rest = numbers
print("a:", a)
print("b:", b)
print("rest", rest)




#SECTION TWO
#Number one
def sum_inner_lists(two_d_list):
    result = []
    for inner in two_d_list:
        result.append(sum(inner))  # sum() handles the inner list
    return result

sample = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(sum_inner_lists(sample))  # Output: [9, 13, 18]


#Number two
def sum_columns(two_d_list):

    return [sum(col) for col in zip(*two_d_list)]

sample = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(sum_columns(sample))  # Output: [7, 14, 19]




#SECTION THREE
#NUMBER ONE
def get_even_numbers():
    return list(filter(lambda x: x % 2 == 0, range(1, 21)))

#NUMBER TWO
def words_longer_than_five(words):
    return list(filter(lambda w: len(w) > 5, words))

#NUMBER THREE
def tuples_first_value_gt_two(tuples_list):
    return list(filter(lambda t: t[0] > 2, tuples_list))

#NUMBER FOUR
def divisible_by_three_and_five():
    return list(filter(lambda x: x % 3 == 0 and x % 5 == 0, range(1, 51)))

#NUMBER FIVE
def filter_palindromes(words):
    return list(filter(lambda w: w == w[::-1], words))




#SECTION FOUR
#NUMBER ONE
def convert_to_uppercase(words):
    return list(map(str.upper, words))

#NUMBER TWO
def square_numbers():
    return list(map(lambda x: x**2, range(1, 11)))

#NUMBER THREE
def capitalize_names(names):
    return list(map(str.capitalize, names))

#NUMBER FOUR
def add_tax(prices):
    return list(map(lambda p: round(p * 1.1, 2), prices))





#SECTION FIVE
#NUMBER ONE
def sum_numbers_1_to_50():
    return reduce(lambda a, b: a + b, range(1, 51))

#NUMBER TWO
def find_max(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

#NUMBER THREE
def concatenate_strings(words):
    return reduce(lambda a, b: a + ' ' + b, words)

#NUMBER FOUR
def product_of_squares(numbers):
    squares = map(lambda x: x**2, numbers)
    return reduce(lambda a, b: a * b, squares)



#SECTION SIX
#NUMBER ONE
def sum_tuples_filter_greater_than_five(tuples_list):
    sums = map(lambda t: t[0] + t[1], tuples_list)
    return list(filter(lambda x: x > 5, sums))

#NUMBER TWO
def sum_numeric_strings(data):
    numeric_strings = filter(lambda x: x.isdigit(), data)
    numbers = map(int, numeric_strings)
    return reduce(lambda a, b: a + b, numbers, 0)





