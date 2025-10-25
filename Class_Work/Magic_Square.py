#create a boolean function to say it is a magic square
#if it is not a matrix or not a type of list, return false
#if size is zero, return false
#create a variable to hold my expected total which we use to check others
#loop through the rows and the columns of the matrix
#if the sum of the rows or columns at any point of size is not equal to my expected total, return false


def is_magic_square(matrix):
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return False

    size = len(matrix)

    if size == 0:
        return False

    if not all(len(row) == size for row in matrix):
        return False

    my_expected_total_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != my_expected_total_sum :
            return False

    for column in range(size):
        if sum(matrix[row][column] for row in range(size)) != my_expected_total_sum:
            return False
    return True



test_list = [
    [2, 3, 5],
    [4, 5, 1],
    [4, 2, 4]
]
print(is_magic_square(test_list))


test_list2 = [
    [5, 2, 5],
    [6, 5, 4],
    [1, 8, 3]
]
print(is_magic_square(test_list2))


test_list3 = [
    [1, 3, 1],
    [3, 1, 1],
    [1, 1, 3]
]
print(is_magic_square(test_list3))


test_diff_list =[
    [2, 1],
    [1, 2]
]
print(is_magic_square(test_diff_list))
