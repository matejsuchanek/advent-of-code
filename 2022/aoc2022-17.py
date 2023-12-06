import os
from itertools import cycle

def provider():
    while True:
        t = top + 4
        yield [(3, t), (4, t), (5, t), (6, t)]

        t = top + 4
        yield [(4, t), (3, t+1), (4, t+1), (5, t+1), (4, t+2)]

        t = top + 4
        yield [(3, t), (4, t), (5, t), (5, t+1), (5, t+2)]

        t = top + 4
        yield [(3, t), (3, t+1), (3, t+2), (3, t+3)]

        t = top + 4
        yield [(3, t), (4, t), (3, t+1), (4, t+1)]


with open(os.path.join('data', 'aoc17.txt'), 'r') as file:
    pattern = file.read().strip()

top = 0
jet = cycle(pattern)
stones = provider()
rest = set()

for _ in range(2022):
    shape = next(stones)
    while True:
        d = next(jet)
        if d == '>':
            new = [(x+1, y) for x, y in shape]
        elif d == '<':
            new = [(x-1, y) for x, y in shape]

        if all(1 <= x <= 7 for x, y in new) \
           and not any(pair in rest for pair in new):
            shape = new

        downward = [(x, y-1) for x, y in shape]
        if any(pair[1] == 0 or pair in rest for pair in downward):
            rest.update(shape)
            top = max(top, max(y for x, y in shape))
            break
        shape = downward

print(top)
