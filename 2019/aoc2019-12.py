import os
import re


def iadd_vector(me, v):
    for i, x in enumerate(v):
        me[i] += v[i]


regex = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>')
moons = []

with open(os.path.join('data', 'aoc12.txt')) as file:
    for line in file:
        moon = list(map(int, regex.fullmatch(line.strip()).groups()))
        moons.append((moon, [0] * 3))

for _ in range(1000):
    changes = []
    for pos, velo in moons:
        change = [0] * 3
        for (other, _) in moons:
            if pos == other:
                continue
            for i, (c1, c2) in enumerate(zip(pos, other)):
                if c2 > c1:
                    change[i] += 1
                elif c2 < c1:
                    change[i] -= 1
        changes.append(change)

    for (pos, velo), change in zip(moons, changes):
        iadd_vector(velo, change)
        iadd_vector(pos, velo)

total = 0
for pos, velo in moons:
    total += sum(map(abs, pos)) * sum(map(abs, velo))

print(total)
