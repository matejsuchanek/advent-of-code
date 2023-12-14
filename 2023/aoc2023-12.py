import re
import os
from collections import deque

splitR = re.compile(r'\.+')

total = 0

with open(os.path.join('data', 'aoc12.txt'), 'r') as file:
    for line in file:
        springs, right = line.split(maxsplit=1)
        counts = [int(x) for x in right.split(',')]
        springs = springs.strip('.')
        goal = len(springs)

        queue = deque([''])

        while queue:
            cur = queue.popleft()
            idx = len(cur)
            if idx == goal:
                blocks = splitR.split(cur.strip('.'))
                total += (counts == list(map(len, blocks)))
            elif springs[idx] == '?':
                queue.append(cur + '.')
                queue.append(cur + '#')
            else:
                queue.append(cur + springs[idx])

print(total)
