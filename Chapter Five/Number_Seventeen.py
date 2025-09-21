# Filter/Map Performance

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

# Step 1: Define functions that do the same as lambdas
def is_odd(x):
    print(f"filter called with: {x}")
    return x % 2 != 0

def square(x):
    print(f"map called with: {x}")
    return x ** 2

# Step 2: Using filter then map (original order)
print("Filter -> Map:")
result1 = list(map(square, filter(is_odd, numbers)))
print("Result:", result1)
print("\n")

# Step 3: Reverse the operations: Map -> Filter
print("Map -> Filter:")
result2 = list(filter(is_odd, map(square, numbers)))
print("Result:", result2)
