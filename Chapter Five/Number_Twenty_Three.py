# (Functional-Style Programming: Order of filter and map Calls)


numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

result1 = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print("Filter -> Map:", result1)


result2 = list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))
print("Map -> Filter:", result2)
