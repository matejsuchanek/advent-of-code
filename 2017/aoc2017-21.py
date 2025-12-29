import os

import numpy as np


def alternatives(recipe):
    for k in range(4):
        base = np.rot90(recipe, k)
        yield base
        yield np.flipud(base)


def pattern_to_array(pattern):
    rows = pattern.split('/')
    n = len(rows)
    array = np.empty((n, n), dtype=bool)
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            array[i, j] = (c == '#')
    return array


recipes_23 = []
recipes_34 = []
with open(os.path.join('data', 'aoc21.txt')) as file:
    for line in map(str.rstrip, file):
        old, _, new = line.partition(' => ')

        old_array = pattern_to_array(old)
        new_array = pattern_to_array(new)

        if old_array.shape == (2, 2):
            for alt in alternatives(old_array):
                recipes_23.append((alt, new_array))
        else:
            for alt in alternatives(old_array):
                recipes_34.append((alt, new_array))

grid = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=bool)

for it in range(18):
    if it == 5:
        print(np.sum(grid))

    if grid.shape[-1] % 2 == 0:
        recipes = recipes_23
        step, mul = (2, 3)
    else:
        recipes = recipes_34
        step, mul = (3, 4)

    new_grid = np.empty(
        ((grid.shape[-2] // step) * mul, (grid.shape[-1] // step) * mul),
        dtype=bool
    )
    for i in range(grid.shape[-2] // step):
        for j in range(grid.shape[-1] // step):
            sub = grid[i*step:(i+1)*step, j*step:(j+1)*step]
            for rec, out in recipes:
                if np.all(sub == rec):
                    new_grid[i*mul:(i+1)*mul, j*mul:(j+1)*mul] = out
                    break

    grid = new_grid

print(np.sum(grid))
