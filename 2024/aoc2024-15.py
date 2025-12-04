import os

from common import Vector

grid = []

pos = None
walls = set()
boxes = set()

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
                walls.add(Vector(i, j))
            elif c == 'O':
                boxes.add(Vector(i, j))
            elif c == '@':
                pos = Vector(i, j)

    steps = ''
    for line in file:
        steps += line.strip()

for step in steps:
    move = moves[step]
    carry = set()
    new = pos
    while True:
        new += move
        if new in walls:
            break

        if new in boxes:
            carry.add(new)
            continue

        if carry:
            boxes -= carry
            boxes |= {x + move for x in carry}
        pos += move
        break

gps = sum(box.x * 100 + box.y for box in boxes)
print(gps)
