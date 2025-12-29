import os
from collections import defaultdict


def dfs(key):
    this = weights[key]
    if not tree[key]:
        return this

    subweights = defaultdict(list)
    for sub in tree[key]:
        subweights[dfs(sub)].append(sub)

    for w, keys in subweights.items():
        if len(keys) == 1:
            odd = keys[0]
            diff = (set(subweights) - {w}).pop() - w
            new = weights[odd] + diff
            print(new)
            this += w + diff
        else:
            this += w * len(keys)

    return this


tree = {}
weights = {}

with open(os.path.join('data', 'aoc7.txt')) as file:
    for line in map(str.rstrip, file):
        left, _, right = line.partition(' -> ')
        disc, _, score = left[:-1].partition(' (')
        weights[disc] = int(score)
        tree[disc] = right.split(', ') if right else []

for key in tree:
    if not any(key in discs for discs in tree.values()):
        print(key)
        dfs(key)
        break
