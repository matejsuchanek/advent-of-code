import math
import os
from collections import Counter
from pprint import pprint


def get_border(rows, which):
    if which == 'top':
        return rows[0]
    elif which == 'bottom':
        return rows[-1]
    elif which == 'left':
        return ''.join(row[0] for row in rows)
    elif which == 'right':
        return ''.join(row[-1] for row in rows)
    raise ValueError(which)


def is_adjacent(first, second, how):
    if how == 'right':
        return get_border(first, 'right') == get_border(second, 'left')
    elif how == 'bottom':
        return get_border(first, 'bottom') == get_border(second, 'top')
    elif how == 'top':
        return get_border(first, 'top') == get_border(second, 'bottom')
    raise ValueError(how)


def get_all_borders(rows):
    return [get_border(rows, which)
            for which in ('top', 'bottom', 'left', 'right')]


def remove_borders(rows):
    return [''.join(row[1:-1]) for row in rows[1:-1]]


def rotate(rows):
    return [''.join(reversed(xyz)) for xyz in zip(*rows)]


def iter_rotations(rows):
    yield rows
    cur = rows
    for _ in range(3):
        cur = rotate(cur)
        yield cur
    cur = rows[::-1]
    yield cur
    for _ in range(3):
        cur = rotate(cur)
        yield cur


def find_tile_for(rows, how, already):
    for tile, other_rows in tiles.items():
        if tile in already:
            continue
        for other_rt in iter_rotations(other_rows):
            if is_adjacent(rows, other_rt, how):
                return tile, other_rt
    return None


def matches(row, monster):
    if len(row) < len(monster):
        return False
    for m, c in zip(monster, row):
        if m == '#' and c != '#':
            return False
    return True


tiles = {}

with open(os.path.join('data', 'aoc20.txt')) as file:
    while True:
        line = next(file, None)
        if line is None:
            break
        tile = int(line.rstrip()[5:-1])
        rows = []
        for line in file:
            line = line.rstrip()
            if not line:
                break
            rows.append(line)
        tiles[tile] = rows

borders_per_tile = {
    tile: get_all_borders(rows)
    for tile, rows in tiles.items()
}

corners = []
for tile, borders in borders_per_tile.items():
    all_borders = set()
    for other_tile, other_borders in borders_per_tile.items():
        if tile == other_tile:
            continue
        all_borders.update(other_borders)
        all_borders.update(x[::-1] for x in other_borders)

    idx = {i for i, border in enumerate(borders) if border in all_borders}
    if len(idx) == 2:
        corners.append(tile)

assert len(corners) == 4
print(math.prod(corners))

first_tile = corners[0]
grid = [[]]
grid_n = [[first_tile]]
already = {first_tile}

for rows in iter_rotations(tiles[first_tile]):
    match = find_tile_for(rows, 'right', already)
    if match:
        grid_n[0].append(match[0])
        grid[0].append(rows)
        grid[0].append(match[1])
        already.add(match[0])
        break

assert len(already) == 2

while grid_n[0][-1] not in corners:
    new_tile, new_rows = find_tile_for(grid[0][-1], 'right', already)
    grid_n[0].append(new_tile)
    grid[0].append(new_rows)
    already.add(new_tile)

if find_tile_for(grid[0][0], 'bottom', already):
    key = 'bottom'
else:
    key = 'top'

n_cols = len(already)
n_rows = len(tiles) // n_cols
for i in range(1, n_rows):
    grid.append([])
    grid_n.append([])
    for j in range(n_cols):
        new_tile, new_rows = find_tile_for(grid[i-1][j], key, already)
        if j > 0:
            assert is_adjacent(grid[i][-1], new_rows, 'right')
        grid[-1].append(new_rows)
        grid_n[-1].append(new_tile)
        already.add(new_tile)

assert grid_n[-1][0] in corners
assert grid_n[-1][-1] in corners
assert len(already) == len(tiles)

if key == 'top':
    grid = [row for row in reversed(grid)]
    grid_n = [row for row in reversed(grid_n)]

trimmed = []
for row in grid:
    for group in zip(*map(remove_borders, row)):
        trimmed.append(''.join(group))

if key == 'top':
    trimmed = trimmed[::-1]

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]

hashes = sum(row.count('#') for row in trimmed)
per_monster = sum(row.count('#') for row in monster)
for rows in iter_rotations(trimmed):
    out = 0
    for i in range(len(rows)-2):
        for j in range(len(rows[i])):
            if all(matches(rows[i+k][j:], monster[k]) for k in range(3)):
                out += 1
    if out > 0:
        print(hashes - per_monster * out)
        break
