from functools import lru_cache


@lru_cache(maxsize=None)
def compute(x, y):
    rack = x + 10
    out = (rack * y + serial) * rack
    return (out // 100) % 10 - 5


def total(x, y, size):
    ret = 0
    for a in range(x, x+size):
        for b in range(y, y+size):
            ret += compute(a, b)
    return ret


serial = int(input())

best = (1, 1)
power = total(1, 1, 3)

for x in range(1, 299):
    for y in range(1, 299):
        energy = total(x, y, 3)
        if energy > power:
            power = energy
            best = (x, y)

print(*best)
