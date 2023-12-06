import os

with open(os.path.join('data', 'aoc5.txt'), 'r') as file:
    seed_line = next(file)
    seeds = [int(x) for x in seed_line.split() if x.isdigit()]
    next(file)  # empty

    for _ in range(7):
        next(file)  # x-to-y map:
        new = seeds[:]
        for line in file:
            if not line.strip():
                break

            dest, source, range_ = map(int, line.split())
            for i, seed in enumerate(seeds):
                if source <= seed < (source + range_):
                    new[i] = dest + (seed - source)
        seeds = new

print(min(seeds))
