import os

with open(os.path.join('data', 'aoc16.txt')) as file:
    init = list(map(int, file.read().strip()))


def pairs(pos, length):
    skip = pos + 1
    repeater = range(skip)
    mult = 1
    while pos < length:
        for _ in repeater:
            yield pos, mult
            pos += 1
        mult = -mult
        pos += skip


def process(signal):
    length = len(signal)
    for phase in range(100):
        new = []
        for pos in range(length):
            out = sum(
                signal[i] * y for i, y in pairs(pos, length) if i < length
            )
            new.append(abs(out) % 10)
        signal = new
    return signal


result = process(init)
print(''.join(str(result[i]) for i in range(8)))
