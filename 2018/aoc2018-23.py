import os
import re


def count_in_range(point):
    in_range = 0
    total = 0
    for bot in bots:
        dist = sum(abs(bot[i] - point[i]) for i in range(3))
        in_range += (dist <= bot[-1])
        total += dist
    return -in_range, dist


highest = 0
best = None

bots = []

lineR = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')
with open(os.path.join('data', 'aoc23.txt')) as file:
    for line in file:
        match = lineR.match(line)

        x, y, z, r = map(int, match.groups())
        bots.append((x, y, z, r))
        if r > highest:
            highest = r
            best = bots[-1]

in_range = 0
for bot in bots:
    dist = sum(abs(bot[i] - best[i]) for i in range(3))
    in_range += (dist <= highest)

print(in_range)

