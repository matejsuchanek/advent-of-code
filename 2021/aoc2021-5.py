from collections import defaultdict
import os

def iter_range(start, stop):
    yield start

    add = 1 if stop > start else -1
    while start != stop:
        start += add
        yield start


lines = []
with open(os.path.join('data', 'aoc5.txt'), 'r') as file:
    for line in file:
        left, right = line.split(' -> ')
        x1, y1 = map(int, left.split(','))
        x2, y2 = map(int, right.split(','))
        quad = (x1, y1, x2, y2)
        lines.append(quad)

counter = defaultdict(lambda: 0)
diagonal = defaultdict(lambda: 0)
for x1, y1, x2, y2 in lines:
    if x1 == x2:
        for i in iter_range(y1, y2):
            counter[x1, i] += 1
            diagonal[x1, i] += 1
    elif y1 == y2:
        for i in iter_range(x1, x2):
            counter[i, y1] += 1
            diagonal[i, y1] += 1
    else:
        for x, y in zip(iter_range(x1, x2), iter_range(y1, y2)):
            diagonal[x, y] += 1

for dd in (counter, diagonal):
    total = 0
    for val in dd.values():
        total += val > 1
    print(total)
