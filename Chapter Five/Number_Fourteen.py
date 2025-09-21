# Is a Sequence Sorted?
def is_ordered(sequence):
    return sequence == sorted(sequence)


# Testing the function
sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 1, 4, 2]
sorted_tuple = (1, 2, 3, 4, 5)
unsorted_tuple = (3, 1, 4, 2)
sorted_string = "abcdef"
unsorted_string = "bacdef"

print(is_ordered(sorted_list)) 
print(is_ordered(unsorted_list))
print(is_ordered(sorted_tuple))
print(is_ordered(unsorted_tuple))
print(is_ordered(sorted_string))
print(is_ordered(unsorted_string))
