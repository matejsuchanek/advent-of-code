import os


def differences(values):
    return [y - x for x, y in zip(values[:-1], values[1:])]


def run(init):
    stack = []
    stack.append(init)
    while True:
        new = differences(stack[-1])
        if all(x == 0 for x in new):
            break
        stack.append(new)

    prev = stack.pop()
    prev.append(prev[-1])
    while stack:
        this = stack.pop()
        this.append(this[-1] + prev[-1])
        prev = this
    return prev[-1]


with open(os.path.join('data', 'aoc9.txt'), 'r') as file:
    prim = sec = 0

    for line in file:
        values = [int(x) for x in line.split()]
        prim += run(values)
        sec += run(values[::-1])

print(prim)
print(sec)
