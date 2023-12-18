import os

diffs = []
steps = (-1, 0, 1)
for dx in steps:
    for dy in steps:
        for dz in steps:
            diffs.append((dx, dy, dz))
diffs.remove((0, 0, 0))

active = set()

with open(os.path.join('data', 'aoc17.txt')) as f:
    z = 0
    for y, line in enumerate(f):
        line = line.rstrip()
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, z))


def get_range_for_index(triples, idx):
    mn = min(tr[idx] for tr in triples)
    mx = max(tr[idx] for tr in triples)
    return range(mn - 1, mx + 2)


for _ in range(6):
    new = set()
    for x in get_range_for_index(active, 0):
        for y in get_range_for_index(active, 1):
            for z in get_range_for_index(active, 2):
                triple = (x, y, z)
                around = 0
                for dx, dy, dz in diffs:
                    other = (x + dx, y + dy, z + dz)
                    around += other in active
                if triple in active and around in (2, 3):
                    new.add(triple)
                elif triple not in active and around == 3:
                    new.add(triple)

    active = new

print(len(active))
