nums = []
for i in range(1, 16):
    nums.append(i)
print("Original list:", nums)

duplicated = []
for n in nums:
    duplicated.append(n)
    duplicated.append(n)
print("Duplicated list:", duplicated)

unique = []
for n in duplicated:
    if n not in unique:
        unique.append(n)
print("List without duplicates:", unique)
