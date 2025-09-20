#Defining the function to return unique sorted values
def unique_sorted(values):
    return sorted(set(values))

#Testing with a list of numbers
numbers = [4, 2, 7, 2, 9, 4, 1]
print(unique_sorted(numbers))

#Testing with a list of strings
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
print(unique_sorted(words))
