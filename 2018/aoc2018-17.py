import os
import re
from collections import deque


clay = set()
water = set()

lineR = re.compile(r'([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)')
with open(os.path.join('data', 'aoc17.txt')) as file:
    for line in file:
        match = lineR.match(line)

        a1, n1, a2, n2, n3 = match.groups()
        if a1 == 'x':
            assert a2 == 'y'
            x, y1, y2 = map(int, (n1, n2, n3))
            for y in range(y1, y2 + 1):
                clay.add((y, x))

        elif a1 == 'y':
            assert a2 == 'x'
            y, x1, x2 = map(int, (n1, n2, n3))
            for x in range(x1, x2 + 1):
                clay.add((y, x))

y_min = min(y for y, x in clay)
y_max = max(y for y, x in clay)

run = True
while run:
    stream = set()
    blocked = []

    queue = deque()
    queue.append((0, 500))
    while queue:
        node = queue.popleft()
        (y, x) = node
        if y > y_max:
            run = False
            continue
        if node in stream:
            continue
        stream.add(node)
        down = (y + 1, x)
        if down in clay or down in water:
            for side in ((y, x - 1), (y, x + 1)):
                if side in clay:
                    blocked.append(node)
                else:
                    queue.append(side)
        else:
            queue.append(down)

    blocked = deque(sorted(blocked))
    while blocked:
        first = blocked.popleft()
        if not blocked:
            break
        second = blocked[0]
        if first[0] != second[0]:
            continue

        level = set()
        for x in range(first[1], second[1] + 1):
            node = (first[0], x)
            if node not in stream:
                break
            level.add(node)
        else:
            water |= level

reached = {node for node in (water | stream) if y_min <= node[0] <= y_max}
print(len(reached))
print(len(water))
