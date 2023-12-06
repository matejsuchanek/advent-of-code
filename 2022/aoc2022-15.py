import os
import re

y = 2_000_000
d = r'(-?\d+)'
regex = re.compile(f'Sensor at x={d}, y={d}: closest beacon is at x={d}, y={d}')

cannot = set()
beacons = set()
sensors = {}
with open(os.path.join('data', 'aoc15.txt'), 'r') as file:
    for line in map(str.rstrip, file):
        match = regex.fullmatch(line)
        sx, sy, bx, by = map(int, match.groups())

        dist = abs(sx - bx) + abs(sy - by)
        diff = dist - abs(y - sy)
        if by == y:
            beacons.add(bx)
        if diff >= 0:
            cannot.update(range(sx - diff, sx + diff + 1))

        sensors[sx, sy] = dist

print(len(cannot - beacons))

stop = False
for y in range(4_000_001):
    x = 0
    while x <= 4_000_000:
        found = False
        for (sx, sy), dist in sensors.items():
            sd = abs(x - sx) + abs(y - sy)
            if sd <= dist:
                x += 1 + dist - sd
                found = True
                break

        if not found:
            print(x * 4_000_000 + y)
            stop = True
            break

    if stop:
        break
