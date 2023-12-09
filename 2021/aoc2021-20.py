import os

image = {}
with open(os.path.join('data', 'aoc20.txt'), 'r') as file:
    algo = next(file).rstrip()
    next(file)
    max_r = 0
    for r, line in enumerate(file):
        max_r = r
        line = line.rstrip()
        for c, char in enumerate(line):
            length = len(line)
            image[r, c] = char
    max_r += 1

span_r = (0, max_r)
span_c = (0, length)

steps = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1), ( 0, 0), ( 0, 1),
    (+1, -1), (+1, 0), (+1, 1),
]

outer = '.'
for i in range(50):
    new = {}
    span_r = (span_r[0] - 1, span_r[1] + 1)
    span_c = (span_c[0] - 1, span_c[1] + 1)

    for r in range(*span_r):
        for c in range(*span_c):
            idx = 0
            for x, y in steps:
                q = (r + x, c + y)
                char = image.get(q, outer)
                idx = 2 * idx + (1 if char == '#' else 0)

            new[r, c] = algo[idx]

    image = new
    if outer == '.':
        outer = algo[0]
    else:
        outer = algo[511]

    if (i+1) in (2, 50):
        print(len([1 for value in image.values() if value == '#']))
