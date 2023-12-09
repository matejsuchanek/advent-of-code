from itertools import permutations
import os

alpha = 'abcdefg'
mapping = {
    frozenset('abcefg'): 0,
    frozenset('cf'): 1,
    frozenset('acdeg'): 2,
    frozenset('acdfg'): 3,
    frozenset('bcdf'): 4,
    frozenset('abdfg'): 5,
    frozenset('abdefg'): 6,
    frozenset('acf'): 7,
    frozenset('abcdefg'): 8,
    frozenset('abcdfg'): 9,
}
unique = {1, 4, 7, 8}
complete = set(mapping)

times = total = 0

with open(os.path.join('data', 'aoc8.txt'), 'r') as file:
    for line in file:
        left, right = line.split(' | ')
        words = left.split()
        for perm in permutations(alpha):
            transp = dict(zip(alpha, perm))
            sets = {frozenset(transp[c] for c in word) for word in words}
            if sets == complete:
                num = 0
                for word in right.split():
                    real = frozenset(transp[c] for c in word)
                    this = mapping[real]
                    if this in unique:
                        times += 1
                    num = num * 10 + this
                total += num
                break

print(times)
print(total)
