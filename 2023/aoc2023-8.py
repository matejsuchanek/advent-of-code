import math
import os

mapping = {}
LR = {'L': 0, 'R': 1}

with open(os.path.join('data', 'aoc8.txt'), 'r') as file:
    instruct = next(file).rstrip()
    next(file)  # empty
    for line in file:
        pos, where = line.rstrip().split(' = ', 1)
        left, right = where[1:-1].split(', ', 1)
        mapping[pos] = (left, right)

curr = 'AAA'
step = 0
while curr != 'ZZZ':
    for x in instruct:
        curr = mapping[curr][LR[x]]
        step += 1
        if curr == 'ZZZ':
            break

print(step)

queue = []

for node in mapping:
    if not node.endswith('A'):
        continue
    seen = {}
    step = 0
    stop = False
    while not stop:
        for i, x in enumerate(instruct):
            node = mapping[node][LR[x]]
            step += 1
            pair = (node, i)
            if pair in seen:
                stop = True
                break
            seen[pair] = step

    for x, j in seen:
        if x.endswith('Z'):
            first = seen[x, j]
            length = step - seen[pair]
            queue.append((first, length))
            break  # it will only work if there is one and only

print(math.lcm(*[l for _, l in queue]))
