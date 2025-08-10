nums = ()

temp_list = []
for i in range(1, 21):
    temp_list.append(i)
nums = tuple(temp_list)
print("Tuple:", nums)

sum_odd_positions = 0
for i in range(1, len(nums), 2):
    sum_odd_positions += nums[i]
print("Sum odd positions:", sum_odd_positions)

sum_even_positions = 0
for i in range(0, len(nums), 2):
    sum_even_positions += nums[i]
print("Sum even positions:", sum_even_positions)

smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n

largest = nums[0]
for n in nums:
    if n > largest:
        largest = n

sum_smallest_largest = smallest + largest
print("Sum smallest and largest:", sum_smallest_largest)

a, b, c, d, e = nums[0], nums[1], nums[2], nums[3], nums[4]
print("First five unpacked:", a, b, c, d, e)
