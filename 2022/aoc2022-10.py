import os

x = 1
i = 0
signal = 0
record = {20, 60, 100, 140, 180, 220}
newline = {40, 80, 120, 160, 200, 240}
screen = ''
with open(os.path.join('data', 'aoc10.txt'), 'r') as file:
    for line in map(str.split, file):
        if line[0] == 'noop':
            cycles = 1
            add = 0
        elif line[0] == 'addx':
            cycles = 2
            add = int(line[1])
        for _ in range(cycles):
            if i in newline:
                screen += '\n'
            if abs(x - i % 40) <= 1:
                screen += '#'
            else:
                screen += ' '
            i += 1
            if i in record:
                signal += x * i

        x += add

print(signal)
print(screen)
