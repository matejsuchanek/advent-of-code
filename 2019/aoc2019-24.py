grid = []

with open(os.path.join('data', 'aoc24.txt')) as file:
    for line in file:
        grid.append(list(line.strip()))

already = set()
already.add(tuple(map(tuple, grid)))

while True:
    new = [None] * len(grid)
    for r, row in enumerate(grid):
        new_row = [None] * len(row)
        for c, tile in enumerate(row):
            bugs = 0
            if r > 0:
                bugs += (grid[r-1][c] == '#')
            if r < len(grid) - 1:
                bugs += (grid[r+1][c] == '#')
            if c > 0:
                bugs += (row[c-1] == '#')
            if c < len(row) - 1:
                bugs += (row[c+1] == '#')
            if tile == '#' and bugs != 1:
                tile = '.'
            elif tile == '.' and bugs in (1, 2):
                tile = '#'
            new_row[c] = tile
        new[r] = new_row
    key = tuple(map(tuple, new))
    if key in already:
        break
    already.add(key)
    grid = new

rating = 0
for r, row in enumerate(new):
    for c, tile in enumerate(row):
        if tile == '#':
            rating += 2 ** (r * len(row) + c)
print(rating)
