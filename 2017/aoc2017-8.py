import os
from collections import defaultdict

my_max = 0
registry = defaultdict(lambda: 0)

with open(os.path.join('data', 'aoc8.txt')) as file:
    for line in file:
        split = line.rstrip().split(maxsplit=5)
        times = -1 if split[1] == 'dec' else 1
        if eval('registry[%r] %s' % tuple(split[4:6])):
            registry[split[0]] += times * int(split[2])
            my_max = max(my_max, registry[split[0]])

print(max(registry.values()))
print(my_max)
