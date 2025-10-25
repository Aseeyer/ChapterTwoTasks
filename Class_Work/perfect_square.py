import math

def get_perfect_square(*numbers):
    results = []
    for number in numbers:
        root = math.isqrt(number)
        results.append(root * root == number)
    return results

print(get_perfect_square(2, 3, 4, 5, 6, 7, 8, 9))
