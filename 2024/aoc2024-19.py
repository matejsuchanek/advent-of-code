import os
from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=1_024 ** 2)
def count_possible(word):
    c = word[0]
    if c not in index:
        return 0

    out = 0
    for p in index[c]:
        if word == p:
            out += 1
        elif word.startswith(p):
            out += count_possible(word[len(p):])

    return out


is_possible = total = 0

index = defaultdict(list)

with open(os.path.join('data', 'aoc19.txt')) as file:
    first = next(file).rstrip()
    for p in first.split(', '):
        index[p[0]].append(p)

    next(file)
    for line in file:
        word = line.rstrip()
        res = count_possible(word)
        is_possible += res > 0
        total += res

print(is_possible)
print(total)
