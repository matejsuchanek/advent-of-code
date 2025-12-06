import math
import os

rows = []

with open(os.path.join('data', 'aoc6.txt')) as file:
    for line in map(str.strip, file):
        if line[0].isdigit():
            rows.append(list(map(int, line.split())))
        else:
            ops = line.split()

total = 0

for op, *nums in zip(ops, *rows):
    if op == '*':
        total += math.prod(nums)
    else:
        total += sum(nums)

print(total)

with open(os.path.join('data', 'aoc6.txt')) as file:
    *lines, last = file.read().splitlines()

total = 0

ops = last.split()
acc = []
pos = 0

for i in range(len(lines[0])):
    cols = ''.join(line[i] for line in lines).strip()
    if cols:
        acc.append(int(cols))
        continue

    if ops[pos] == '*':
        total += math.prod(acc)
    else:
        total += sum(acc)
    pos += 1
    acc = []

if acc:
    if ops[pos] == '*':
        total += math.prod(acc)
    else:
        total += sum(acc)

print(total)
