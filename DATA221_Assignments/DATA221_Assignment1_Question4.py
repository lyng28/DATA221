# Sorted Search with Condition

from random import random

values = [random() for i in range(20)]
x = random()

sorted_list = sorted(values)
matching_indices = []
for index_value in range(len(sorted_list)):
    if sorted_list[index_value] >= x:
        matching_indices.append(index_value)

print("Sorted list: ", sorted_list)
print("x :", x)

if len(matching_indices) < 0:
    print("First matching indices: ", matching_indices)
else:
    print("No matching indices")