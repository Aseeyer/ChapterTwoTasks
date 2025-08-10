import random

nums = [random.randint(1, 50) for _ in range(10)]
print("List:", nums)

count = 0
for _ in nums:
    count += 1
print("Length:", count)


sum_even_positions = 0
for i in range(0, count, 2):
    sum_even_positions += nums[i]
print("Sum even positions:", sum_even_positions)


sum_odd_positions = 0
for i in range(1, count, 2):
    sum_odd_positions += nums[i]
print("Sum odd positions:", sum_odd_positions)

product_third_positions = 1
for i in range(2, count, 3):
    product_third_positions *= nums[i]
print("Product every third position:", product_third_positions)


total_sum = 0
for n in nums:
    total_sum += n
average = total_sum / count
print("Average:", average)

largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest:", largest)

smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n
print("Smallest:", smallest)



strings = ["abc", "xyz", "aba", "128721", "aa", "bcb", "x"]

count = 0
result_strings = []

for s in strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1
        result_strings.append(s)

print("Count:", count)
print("Strings:", result_strings)

