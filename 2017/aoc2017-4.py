import os

result = result_2 = 0

with open(os.path.join('data', 'aoc4.txt')) as file:
    for line in file:
        split = line.split()
        sets = list(map(frozenset, split))
        result += len(set(split)) == len(split)
        result_2 += len(set(sets)) == len(sets)

print(result)
print(result_2)
