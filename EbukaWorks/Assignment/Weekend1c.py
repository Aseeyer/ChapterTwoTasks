def sum_every_third(lst):
    total = 0
    index = 2
    while index < len(lst):
        total += lst[index]
        index += 3
    return total

def sum_first_middle_last(lst):
    if len(lst) == 0:
        return 0
    first = lst[0]
    last = lst[-1]

    if len(lst) % 2 == 1:
        middle = lst[len(lst) // 2]
    else:
        mid1 = lst[(len(lst) // 2) - 1]
        mid2 = lst[len(lst) // 2]
        middle = (mid1 + mid2) / 2

    return first + middle + last




numbers = [1, 2, 3, 4, 5, 6, 7]

print("Sum of every third element:", sum_every_third(numbers))
print("Sum of first, middle, last:", sum_first_middle_last(numbers))
