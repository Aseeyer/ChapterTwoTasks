"""
5.1
#A
day, high_temperature = ('Monday', 87, 65)
The tuple on the right has 3 elements: 'Monday', 87, and 65.
But on the left, they’re trying to unpack into only 2 variables (day and high_temperature).
Python requires the number of variables to match the number of items in the tuple.


#B
numbers = [1, 2, 3, 4, 5]
numbers[10]
The list numbers has indices 0 to 4 (five elements). numbers[10] tries to access index 10, which doesn’t exist.
Python will raise IndexError: list index out of range.


#C
name = 'amanda'
name[0] = 'A'
Strings are immutable in Python. This means you cannot change a character in a string by assignment.
Python will raise TypeError: 'str' object does not support item assignment.


#D
numbers = [1, 2, 3, 4, 5]
numbers[3.4]
List indices must be integers or slices, not floats.
Python will raise TypeError: list indices must be integers or slices, not float.


#E
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[0] = 'Ariana'
Tuples are immutable. You cannot change their elements after creation.
Python will raise TypeError: 'tuple' object does not support item assignment.


#F
('Monday', 87, 65) + 'Tuesday'
You cannot concatenate a tuple with a string. They are different data types.
Python will raise TypeError: can only concatenate tuple (not "str") to tuple.


#G
'A' += ('B', 'C')
You cannot add a string and a tuple using += or +.
Python will raise TypeError: can only concatenate str (not "tuple") to str.


#H
x = 7
del x
print(x)
After using del x, the variable x is removed from memory.
Python will raise NameError: name 'x' is not defined.


#I
numbers = [1, 2, 3, 4, 5]
numbers.index(10)
The value 10 is not in the list, so index() cannot find it.
Python will raise ValueError: 10 is not in list.


#J
numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)
extend() takes a single iterable, not multiple arguments.
Python will raise TypeError: list.extend() takes exactly one argument (3 given).


#K
numbers = [1, 2, 3, 4, 5]
numbers.remove(10)
remove() tries to delete the given value, but 10 is not in the list.
Python will raise ValueError: list.remove(x): x not in list.


#L
values = []
values.pop()
pop() tries to remove and return the last item of the list.
If the list is empty, Python will raise IndexError: pop from empty list.


"""
