import os
import re

result = 0
patternR = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

with open(os.path.join('data', 'aoc3.txt')) as file:
    line = file.read()

found = []

for needle, val in [
    ("do()", True),
    ("don't()", False),
]:
    pos = 0
    while True:
        pos = line.find(needle, pos)
        if pos == -1:
            break
        found.append((pos, 'do', val))
        pos += 1

for match in patternR.finditer(line):
    x, y = map(int, match.groups())
    mul = x * y
    result += mul
    found.append((match.start(), 'mul', mul))

print(result)

result = 0
found.sort()

enabled = True
for _, what, val in found:
    if what == 'do':
        enabled = val
    elif what == 'mul' and enabled:
        result += val

print(result)
