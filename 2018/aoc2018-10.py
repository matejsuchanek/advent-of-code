import os
import re

points = []
regex = re.compile(r'position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>')

with open(os.path.join('data', 'aoc10.txt')) as file:
    for match in map(regex.match, file):
        x, y, v_x, v_y = map(int, match.groups())
        points.append([x, y, v_x, v_y])

best = float('inf')
out = 0
while True:
    dist = 0
    for (x1, y1, _, _) in points:
        for (x2, y2, _, _) in points:
            d = abs(x1 - x2) + abs(y1 - y2)
            dist = max(dist, d)

    if dist > best:
        break

    best = dist

    steps = 100 if dist > 2000 else 1  # GUESS!
    for p in points:
        p[0] += p[2] * steps
        p[1] += p[3] * steps
    out += steps

for p in points:
    p[0] -= p[2]
    p[1] -= p[3]
out -= 1

hashes = {(x, y) for (x, y, _, _) in points}

left = min(p[0] for p in points)
right = max(p[0] for p in points)
top = min(p[1] for p in points)
bottom = max(p[1] for p in points)
for y in range(top, bottom+1):
    for x in range(left, right+1):
        if (x, y) in hashes:
            print('#', end='')
        else:
            print('.', end='')
    print()

print(out)
