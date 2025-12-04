import os
from collections import defaultdict
from itertools import combinations

from common import Vector

antennas = defaultdict(list)
antinodes = set()

X = Y = 0

with open(os.path.join('data', 'aoc8.txt')) as file:
    for i, line in enumerate(file):
        line = line.rstrip()
        X = i
        Y = max(Y, len(line))

        for j, c in enumerate(line):
            if c != '.':
                antennas[c].append(Vector(i, j))

for values in antennas.values():
    for first, second in combinations(values, 2):
        for node in [2 * second - first, 2 * first - second]:
            if 0 <= node.x <= X and 0 <= node.y < Y:
                antinodes.add(node)

print(len(antinodes))
