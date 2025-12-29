import os

UP, RIGHT, DOWN, LEFT = range(4)
facing = [(-1, 0), (0, 1), (1, 0), (0, -1)]
go = UP

infected = set()
with open(os.path.join('data', 'aoc22.txt')) as file:
    for row, line in enumerate(map(str.rstrip, file)):
        width = len(line)
        infected.update(
            (row, col) for col, char in enumerate(line) if char == '#'
        )
    pos = (row // 2, width // 2)

print(infected)
print(pos)

count = 0
for _ in range(10000):
    if pos in infected:
        go = (go + 1) % 4
        infected.remove(pos)
    else:
        go = (go - 1) % 4
        infected.add(pos)
        count += 1
    pos = (pos[0] + facing[go][0], pos[1] + facing[go][1])

print(count)
