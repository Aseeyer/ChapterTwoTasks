#Given a list of numbers, write a python function using map() that squares each number in the list
#numbers = [1, 2, 3, 4, 5]
#output = numbers = [1, 4, 9, 16, 25]

def get_square(numbers):
    return list(map(pow, numbers, [2]*len(numbers)))

numbers = [1, 2, 3, 4, 5]
print(get_square(numbers))




#write a python function that converts a list of strings to their corresponding lengths using the map() function.
#words = ["apple", "banana", "cherry"]
#output: [5, 6, 6]

def words_to_lengths(words):
    return list(map(len, words))

words = ["apple", "banana", "cherry"]
print(words_to_lengths(words))




#Write a python function using filter() that returns a list of all the even numbers from a given list of intergers
#numbers = [1, 2, 3, 4, 5, 6]
#output =: [2, 4, 6]

def is_single_even(number):
    return number % 2 == 0

def is_Even(numbers):
    return list(filter(is_single_even, numbers))

numbers = [1, 2, 3, 4, 5, 6]
print(is_Even(numbers))





#Using filter(), create a python function that filters out all the words with more than 5 characters from the following list
#sample: words = ["apple", "banana", "kiwi", "grapes", "cherry"]



def filter_short_words(words):
    return list(filter(lambda w: len(w) <= 5, words))


words = ["apple", "banana", "kiwi", "grapes", "cherry"]
print(filter_short_words(words)) 

    