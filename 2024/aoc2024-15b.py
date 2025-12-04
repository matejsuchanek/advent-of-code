import os
from collections import deque

from common import Vector

grid = []

pos = None
walls = set()
boxes = {}

moves = {
    '^': Vector(-1, 0),
    '>': Vector(0, +1),
    'v': Vector(+1, 0),
    '<': Vector(0, -1),
}

with open(os.path.join('data', 'aoc15.txt')) as file:
    for i, line in enumerate(file):
        if line.rstrip() == '':
            break

        for j, c in enumerate(line.rstrip()):
            if c == '#':
                walls.add(Vector(i, 2*j))
                walls.add(Vector(i, 2*j+1))
            elif c == 'O':
                boxes[Vector(i, 2*j)] = '['
                boxes[Vector(i, 2*j+1)] = ']'
            elif c == '@':
                pos = Vector(i, 2*j)

    steps = ''
    for line in file:
        steps += line.strip()

for step in steps:
    move = moves[step]
    new = pos + move
    if new in walls:
        continue
    if new not in boxes:
        pos = new
        continue

    carry = {}
    queue = deque()
    queue.append(new)
    ok = True
    while ok and queue:
        node = queue.popleft()
        if node in carry:
            continue

        new = node + move
        if new in walls:
            ok = False
            break

        carry[node] = boxes[node]
        if boxes[node] == ']':
            queue.append(node + moves['<'])
        elif boxes[node] == '[':
            queue.append(node + moves['>'])

        if new in boxes:
            queue.append(new)

    if ok:
        for node in carry:
            boxes.pop(node)
        for node in carry:
            boxes[node + move] = carry[node]
        pos += move

gps = sum(node.x * 100 + node.y for node in boxes if boxes[node] == '[')
print(gps)
