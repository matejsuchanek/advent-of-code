import os

diffs = []
steps = (-1, 0, 1)
for dx in steps:
    for dy in steps:
        for dz in steps:
            for dw in steps:
                diffs.append((dx, dy, dz, dw))
diffs.remove((0, 0, 0, 0))

active = set()

with open(os.path.join('data', 'aoc17.txt')) as f:
    w = z = 0
    for y, line in enumerate(f):
        line = line.rstrip()
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, z, w))


def get_range_for_index(triples, idx):
    mn = min(tr[idx] for tr in triples)
    mx = max(tr[idx] for tr in triples)
    return range(mn - 1, mx + 2)


for _ in range(6):
    new = set()
    for x in get_range_for_index(active, 0):
        for y in get_range_for_index(active, 1):
            for z in get_range_for_index(active, 2):
                for w in get_range_for_index(active, 3):
                    coord = (x, y, z, w)
                    around = 0
                    for dx, dy, dz, dw in diffs:
                        other = (x + dx, y + dy, z + dz, w + dw)
                        around += other in active
                    if coord in active and around in (2, 3):
                        new.add(coord)
                    elif coord not in active and around == 3:
                        new.add(coord)

    active = new

print(len(active))
