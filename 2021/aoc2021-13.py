import os

dots = set()

with open(os.path.join('data', 'aoc13.txt'), 'r') as file:
    for line in file:
        line = line.rstrip()
        if not line:
            break

        x, y = map(int, line.split(','))
        dots.add((x, y))

    for i, line in enumerate(file):
        new = set()
        fold, along, axis = line.split()
        ax, n = axis.split('=')
        n = int(n)
        if ax == 'y':
            for pos in dots:
                x, y = pos
                if y > n:
                    new_y = n + n - y
                    new.add((x, new_y))
                else:
                    new.add(pos)
        elif ax == 'x':
            for pos in dots:
                x, y = pos
                if x > n:
                    new_x = n + n - x
                    new.add((new_x, y))
                else:
                    new.add(pos)

        dots = new
        if i == 0:
            print(len(dots))

max_x = max(x for x, y in dots) + 1
max_y = max(y for x, y in dots) + 1
for y in range(max_y):
    line = ''
    for x in range(max_x):
        line += '#' if (x, y) in dots else ' '
    print(line)
