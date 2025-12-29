import os
from functools import lru_cache


@lru_cache(maxsize=None)
def compute(x, y):
    return (abs(x) - abs(y)) // 2 + abs(y)


with open(os.path.join('data', 'aoc11.txt')) as file:
    string = next(file).strip()

dirs = {
    'n':  (2,  0),
    'ne': (1,  1),
    'nw': (1, -1),
    's':  (-2, 0),
    'se': (-1, 1),
    'sw': (-1, -1),
}

x, y = 0, 0
max_dist = compute(x, y)

for step in string.split(','):
    x += dirs[step][0]
    y += dirs[step][1]
    max_dist = max(max_dist, compute(x, y))

print(compute(x, y))
print(max_dist)
