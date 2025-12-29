import os

moves = []
with open(os.path.join('data', 'aoc16.txt')) as file:
    for inst in next(file).strip().split(','):
        if inst.startswith('s'):
            moves.append((inst[0], int(inst[1:])))
        elif inst.startswith('x'):
            a, b = list(map(int, inst[1:].split('/')))
            moves.append((inst[0], a, b))
        elif inst.startswith('p'):
            a, b = inst[1:].split('/')
            moves.append((inst[0], a, b))

positions_raw = 'abcdefghijklmnop'
length = len(positions_raw)

cache = {}

for i in range(10 ** 9):
    if positions_raw in cache:
        positions_raw = cache[positions_raw]
        continue

    positions = list(positions_raw)
    for inst, *args in moves:
        if inst == 's':
            x, = args
            new_tail = positions[:-x]
            del positions[:-x]
            positions.extend(new_tail)
        elif inst == 'x':
            a, b = args
            tmp = positions[a]
            positions[a] = positions[b]
            positions[b] = tmp
        elif inst == 'p':
            a, b = args
            idx = positions.index(b)
            positions[positions.index(a)] = b
            positions[idx] = a

    new = ''.join(positions)
    if not cache:
        print(new)
    cache[positions_raw] = new
    positions_raw = new
    del positions

print(positions_raw)
