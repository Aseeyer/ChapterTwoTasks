#Sorting Letters and Removing Duplicates
import random

letters = [random.choice(['a', 'b', 'c', 'd', 'e', 'f']) for _ in range(20)]
print("Original list:", letters)

# a) Sort the list in ascending order
ascending = sorted(letters)
print("Ascending order:", ascending)



# b) Sort the list in descending order
descending = sorted(letters, reverse=True)
print("Descending order:", descending)



# c) Get the unique values and sort them in ascending order
unique_sorted = sorted(set(letters))
print("Unique values sorted:", unique_sorted)
