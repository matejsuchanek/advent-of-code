import os

with open(os.path.join('data', 'aoc3.txt')) as file:
    wire1, wire2 = file.read().splitlines()

times1 = {}
times2 = {}

for wire, times in zip((wire1, wire2), (times1, times2)):
    pos_x = pos_y = steps = 0
    for move in wire.split(','):
        d, n = move[:1], int(move[1:])
        if d == 'R':
            x, y = 1, 0
        elif d == 'L':
            x, y = -1, 0
        elif d == 'U':
            x, y = 0, 1
        elif d == 'D':
            x, y = 0, -1
        for _ in range(n):
            steps += 1
            pos_x += x
            pos_y += y
            if (pos_x, pos_y) not in times:
                times[pos_x, pos_y] = steps

inter = times1.keys() & times2.keys()
print(min(abs(x) + abs(y) for x, y in inter))
print(min(times1[k] + times2[k] for k in inter))
