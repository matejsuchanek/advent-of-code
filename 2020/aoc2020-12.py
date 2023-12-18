import os

EAST, SOUTH, WEST, NORTH = range(4)
dirs = {
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
    NORTH: (0, 1)
}
c_to_dir = {'N': NORTH, 'E': EAST, 'S': SOUTH, 'W': WEST}

face = EAST
pos = (0, 0)

with open(os.path.join('data', 'aoc12.txt')) as f:
    for line in f:
        line = line.rstrip()
        c, num = line[0], int(line[1:])
        if c in c_to_dir or c == 'F':
            x, y = dirs[face if c == 'F' else c_to_dir[c]]
            pos = (pos[0] + x * num, pos[1] + y * num)
        elif c in ('L', 'R'):
            face = (face + (-1 if c == 'L' else 1) * (num // 90)) % 4

print(abs(pos[0]) + abs(pos[1]))
