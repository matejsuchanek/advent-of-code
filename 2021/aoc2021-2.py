import os

pos = 0
depth = 0
lines = []
with open(os.path.join('data', 'aoc2.txt'), 'r') as file:
    for line in file:
        lines.append(line)
        com, n = line.split()
        if com == 'forward':
            pos += int(n)
        elif com == 'down':
            depth += int(n)
        elif com == 'up':
            depth -= int(n)

print(pos * depth)

pos = 0
depth = 0
aim = 0
for line in lines:
    com, n = line.split()
    if com == 'forward':
        pos += int(n)
        depth += int(n) * aim
    elif com == 'down':
        aim += int(n)
    elif com == 'up':
        aim -= int(n)

print(pos * depth)
