import os

UP, RIGHT, DOWN, LEFT = range(4)
facing = [(-1, 0), (0, 1), (1, 0), (0, -1)]
go = UP

weakened = set()
infected = set()
flagged = set()
with open(os.path.join('data', 'aoc22.txt')) as file:
    for row, line in enumerate(map(str.rstrip, file)):
        width = len(line)
        infected.update(
            (row, col) for col, char in enumerate(line) if char == '#'
        )
    pos = (row // 2, width // 2)

count = 0
for _ in range(10_000_000):
    if pos in weakened:
        weakened.remove(pos)
        infected.add(pos)
        count += 1
    elif pos in infected:
        infected.remove(pos)
        flagged.add(pos)
        go = (go + 1) % 4
    elif pos in flagged:
        flagged.remove(pos)
        go = (go + 2) % 4
    else:
        weakened.add(pos)
        go = (go + 3) % 4
    pos = (pos[0] + facing[go][0], pos[1] + facing[go][1])

print(count)
