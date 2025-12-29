import os
from itertools import permutations

result = result_2 = 0

with open(os.path.join('data', 'aoc2.txt')) as file:
    for line in map(str.rstrip, file):
        ints = list(map(int, line.split()))
        result += max(ints) - min(ints)
        for x, y in permutations(ints, 2):
            div, mod = divmod(x, y)
            if mod == 0:
                result_2 += div

print(result)
print(result_2)
