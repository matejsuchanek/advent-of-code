import os

prio = {c: i for i, c in enumerate(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}

total = 0
groups = []
with open(os.path.join('data', 'aoc3.txt'), 'r') as file:
    group = []
    for line in map(str.strip, file):
        half = len(line) // 2
        first = set(line[:half])
        second = set(line[half:])
        intersect = first & second
        total += prio[intersect.pop()]
        group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []

print(total)

total = 0
for group in groups:
    intersect = set.intersection(*map(set, group))
    total += prio[intersect.pop()]

print(total)
