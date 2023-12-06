import os
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]
    for x, y in zip(left, right):
        cmp = compare(x, y)
        if cmp != 0:
            return cmp

    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


in_order = []
packets = [
    [[2]],
    [[6]],
]
with open(os.path.join('data', 'aoc13.txt'), 'r') as file:
    it = map(str.rstrip, file)
    i = 1
    while True:
        line = next(it)
        loc = {}
        exec(f'left = {line}', {}, loc)

        line = next(it)
        exec(f'right = {line}', {}, loc)

        packets.append(loc['left'])
        packets.append(loc['right'])
        if compare(loc['left'], loc['right']) == -1:
            in_order.append(i)

        if next(it, None) is None:
            break

        i += 1

print(sum(in_order))

packets.sort(key=cmp_to_key(compare))
prod = 1
for i, p in enumerate(packets, start=1):
    if p == [[2]] or p == [[6]]:
        prod *= i
print(prod)
