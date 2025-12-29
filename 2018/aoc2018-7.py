import os
from collections import defaultdict


incoming = defaultdict(set)
outgoing = defaultdict(set)
nodes = set()
with open(os.path.join('data', 'aoc7.txt')) as file:
    for line in file:
        parts = line.split()
        start, end = parts[1], parts[7]
        nodes.add(start)
        nodes.add(end)
        incoming[end].add(start)
        outgoing[start].add(end)

out = ''
while nodes:
    for key in sorted(nodes):
        if incoming[key]:
            continue
        nodes.discard(key)
        out += key
        for other in outgoing[key]:
            incoming[other].discard(key)
        break

print(out)
