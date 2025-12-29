import os
from math import inf

centers = []
points = {}

with open(os.path.join('data', 'aoc6.txt')) as file:
    for line in map(str.strip, file):
        x, y = map(int, line.split(', '))
        centers.append((x, y))

left = min(c[0] for c in centers) - 1
right = max(c[0] for c in centers) + 1
top = min(c[1] for c in centers) - 1
bottom = max(c[1] for c in centers) + 1
out = 0

for y in range(top, bottom+1):
    for x in range(left, right+1):
        best = inf
        who = None
        total = 0
        for i, (cx, cy) in enumerate(centers):
            dist = abs(cx - x) + abs(cy - y)
            total += dist
            if dist < best:
                best = dist
                who = i
            elif dist == best:
                who = None
        points[x, y] = (best, who)
        if total < 10000:
            out += 1

border = set()
for y in range(top, bottom+1):
    border.add(points[left,  y][1])
    border.add(points[right, y][1])
for x in range(left, right+1):
    border.add(points[x, top][1])
    border.add(points[x, bottom][1])

counts = dict.fromkeys(set(range(len(centers))) - border, 0)
for _, who in points.values():
    if who in counts:
        counts[who] += 1

print(max(counts.values()))
print(out)
