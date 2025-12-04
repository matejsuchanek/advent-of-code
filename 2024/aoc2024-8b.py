import os
from collections import defaultdict
from itertools import combinations
from math import gcd

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
    if len(values) < 2:
        continue
    for first, second in combinations(values, 2):
        diff = second - first
        diff //= gcd(diff.x, diff.y)

        antinodes.add(first)
        for mul in (+1, -1):
            aux = first
            while True:
                aux += mul * diff
                if not (0 <= aux.x <= X) or not (0 <= aux.y < Y):
                    break
                antinodes.add(aux)

print(len(antinodes))
