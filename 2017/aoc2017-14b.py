from collections import deque

from knot_hash import knot_hash


def moves(x, y):
    yield (x - 1, y)
    yield (x + 1, y)
    yield (x, y - 1)
    yield (x, y + 1)


string = input()

to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
}

grid = []

for i in range(128):
    h = knot_hash(f'{string}-{i}')
    grid.append(list(''.join(map(to_bin.get, h))))

queue = deque()
out = 0

for x in range(128):
    for y in range(128):
        bit = grid[x][y]
        if bit == '0' or bit == 'x':
            continue
        queue.append((x, y))
        grid[x][y] = 'x'
        while len(queue):
            for i, j in moves(*queue.popleft()):
                if 0 <= i < 128 and 0 <= j < 128:
                    if grid[i][j] == '1':
                        grid[i][j] = 'x'
                        queue.append((i, j))
        out += 1

print(out)
