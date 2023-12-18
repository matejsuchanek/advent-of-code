import os

rows = []
with open(os.path.join('data', 'aoc11.txt')) as f:
    for line in f:
        rows.append(line.rstrip())

diffs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

while True:
    new = []
    for i, row in enumerate(rows):
        new_row = ''
        for j, c in enumerate(row):
            occ = 0
            for di, dj in diffs:
                new_i, new_j = i + di, j + dj
                while 0 <= new_i < len(rows) and 0 <= new_j < len(row):
                    pos = rows[new_i][new_j]
                    if pos != '.':
                        occ += pos == '#'
                        break
                    new_i += di
                    new_j += dj
            if c == 'L' and occ == 0:
                new_row += '#'
            elif c == '#' and occ >= 5:
                new_row += 'L'
            else:
                new_row += c
        new.append(new_row)

    if new == rows:
        result = sum(row.count('#') for row in rows)
        print(result)
        break
    rows = new
