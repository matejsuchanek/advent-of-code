import os

dirs = {
    'e': (2, 0),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
    'se': (1, -1),
    'sw': (-1, -1),
}

black = set()

with open(os.path.join('data', 'aoc24.txt')) as f:
    for line in f:
        line = line.rstrip()
        length = len(line)
        index = 0
        coord = (0, 0)
        while index < length:
            for key, (x, y) in dirs.items():
                if line[index:].startswith(key):
                    coord = (coord[0] + x, coord[1] + y)
                    index += len(key)
                    break
        if coord in black:
            black.remove(coord)
        else:
            black.add(coord)

print(len(black))

for i in range(100):
    positions = set()
    for coord in black:
        positions.add(coord)
        for (x, y) in dirs.values():
            positions.add((coord[0] + x, coord[1] + y))

    add = set()
    remove = set()
    for coord in positions:
        around = 0
        for (x, y) in dirs.values():
            adj = (coord[0] + x, coord[1] + y)
            around += adj in black
        if coord in black and (around == 0 or around > 2):
            remove.add(coord)
        elif coord not in black and around == 2:
            add.add(coord)
    black |= add
    black -= remove

print(len(black))
