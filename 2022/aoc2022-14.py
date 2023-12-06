import os

state = {}
with open(os.path.join('data', 'aoc14.txt'), 'r') as file:
    for line in map(str.rstrip, file):
        pairs = [x.split(',') for x in line.split(' -> ')]
        pairs = [(int(x), int(y)) for x, y in pairs]
        prev = pairs[0]
        for pair in pairs[1:]:
            if prev[0] == pair[0]:
                x = pair[0]
                a = min(prev[1], pair[1])
                b = max(prev[1], pair[1])
                for y in range(a, b+1):
                    state[x, y] = '#'
            elif prev[1] == pair[1]:
                y = pair[1]
                a = min(prev[0], pair[0])
                b = max(prev[0], pair[0])
                for x in range(a, b+1):
                    state[x, y] = '#'
            prev = pair

lowest = max(y for x, y in state)
floor = lowest + 2
rest = 0
reported = False

while (500, 0) not in state:
    x = 500
    y = 0
    while True:
        ny = y + 1
        if ny < floor:
            if (x, ny) not in state:
                y = ny
                continue

            nx = x - 1
            if (nx, ny) not in state:
                x, y = nx, ny
                continue

            nx = x + 1
            if (nx, ny) not in state:
                x, y = nx, ny
                continue

        state[x, y] = 'o'
        rest += 1
        break

    if y >= lowest and not reported:
        reported = True
        print(rest)

print(rest)
