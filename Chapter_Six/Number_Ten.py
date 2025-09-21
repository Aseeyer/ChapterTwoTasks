# (Set Manipulations)

set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

print(set1)
print(set2)

print("a) Comparison Operators")
print("set1 == set2:", set1 == set2)
print("set1 != set2:", set1 != set2)
print("set1 < set2:", set1 < set2)
print("set1 <= set2:", set1 <= set2)
print("set1 > set2:", set1 > set2)
print("set1 >= set2:", set1 >= set2)

print("\nb) Mathematical Set Operators")
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Difference (set2 - set1):", set2 - set1)
print("Symmetric Difference:", set1 ^ set2)
