import os

with open(os.path.join('data', 'aoc5.txt'), 'r') as file:
    seed_line = next(file)
    seeds = [int(x) for x in seed_line.split() if x.isdigit()]
    tuples = list(zip(seeds[0::2], seeds[1::2], strict=True))
    next(file)  # empty

    for _ in range(7):
        next(file)  # x-to-y map:
        mapped = []
        for line in file:
            if not line.strip():
                break

            dest, source, range_ = map(int, line.split())
            source_end = source + range_
            dest_end = dest + range_
            left = []

            for t in tuples:
                start, num = t
                end = start + num
                if source <= start < source_end:
                    new_start = dest + start - source
                    if end <= source_end:
                        mapped.append((new_start, num))
                    else:
                        mapped.append((new_start, source_end - start))
                        left.append((source_end, end - source_end))

                elif source < end <= source_end:
                    mapped.append((dest, end - source))
                    left.append((start, source - start))
                elif start < source and source_end < end:
                    mapped.append((dest, range_))
                    left.append((start, source - start))
                    left.append((source_end, end - source_end))
                else:
                    left.append(t)

            tuples = left

        tuples += mapped

print(min(t[0] for t in tuples))
