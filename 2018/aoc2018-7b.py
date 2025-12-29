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

seconds = 0
workers = [[0, ' '] for _ in range(5)]
while True:
    for i, (s, k) in enumerate(workers):
        if s:
            workers[i][0] -= 1
            if not workers[i][0]:
                workers[i][1] = ' '
                for other in outgoing[k]:
                    incoming[other].discard(k)

    for key in sorted(nodes):
        if incoming[key]:
            continue
        for i, (s, k) in enumerate(workers):
            if not s:
                workers[i][0] = ord(key) - 4
                workers[i][1] = key
                nodes.discard(key)
                break

    if all(s == 0 for (s, k) in workers):
        break
    seconds += 1

print(seconds)
