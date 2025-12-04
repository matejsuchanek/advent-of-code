import os

from common import Vector, looks_diag

lines = []
with open(os.path.join('data', 'aoc4.txt')) as file:
    for line in file:
        lines.append(line.strip())

result = 0

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        vec = Vector(x, y)
        for move in looks_diag:
            for i, c in enumerate('XMAS'):
                new = vec + i * move
                if 0 <= new.x < len(lines) \
                   and 0 <= new.y < len(lines[new.x]) \
                   and lines[new.x][new.y] == c:
                    if c == 'S':
                        result += 1
                else:
                    break

print(result)

result = 0
order = [
    Vector(-1, -1),
    Vector(-1, +1),
    Vector(+1, -1),
    Vector(+1, +1),
]
words = {'MMSS', 'MSMS', 'SSMM', 'SMSM'}

for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[x]) - 1):
        vec = Vector(x, y)
        c = lines[x][y]
        if c != 'A':
            continue
        w = ''
        for move in order:
            new = vec + move
            w += lines[new.x][new.y]
        if w in words:
            result += 1

print(result)
