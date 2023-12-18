import os

EAST, SOUTH, WEST, NORTH = range(4)
dirs = {
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
    NORTH: (0, 1)
}
c_to_dir = {'N': NORTH, 'E': EAST, 'S': SOUTH, 'W': WEST}

waypoint = (10, 1)
pos = (0, 0)

with open(os.path.join('data', 'aoc12.txt')) as f:
    for line in f:
        line = line.rstrip()
        c, num = line[0], int(line[1:])
        if c in c_to_dir:
            x, y = dirs[c_to_dir[c]]
            waypoint = (waypoint[0] + x * num, waypoint[1] + y * num)
        elif c in ('L', 'R'):
            right = ((-1 if c == 'L' else 1) * (num // 90)) % 4
            if right == 1:
                waypoint = (waypoint[1], -waypoint[0])
            elif right == 2:
                waypoint = (-waypoint[0], -waypoint[1])
            elif right == 3:
                waypoint = (-waypoint[1], waypoint[0])
        elif c == 'F':
            pos = (pos[0] + num * waypoint[0], pos[1] + num * waypoint[1])

print(abs(pos[0]) + abs(pos[1]))
