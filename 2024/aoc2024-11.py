import os

with open(os.path.join('data', 'aoc11.txt')) as file:
    stones = [int(x) for x in file.read().split()]

for _ in range(25):
    new = []
    for val in stones:
        length = len(str(val))
        if val == 0:
            new.append(1)
        elif length % 2 == 0:
            div, mod = divmod(val, 10 ** (length // 2))
            new.append(div)
            new.append(mod)
        else:
            new.append(val * 2024)

    stones = new
    del new

print(len(stones))
