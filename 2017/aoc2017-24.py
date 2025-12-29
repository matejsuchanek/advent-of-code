import os
from collections import defaultdict


def dfs(this, already, score):
    pairs = [pair for pair in lookup[this] if pair not in already]
    if not pairs:
        by_length[len(already)].append(score)
        return score

    best = score
    for pair in pairs:
        already.add(pair)
        n = pair[1] if pair[1] != this else pair[0]
        out = dfs(n, already, score + sum(pair))
        already.remove(pair)
        best = max(best, out)

    return best


lookup = defaultdict(list)
with open(os.path.join('data', 'aoc24.txt')) as file:
    for line in map(str.rstrip, file):
        x, y = map(int, line.split('/'))
        pair = (x, y)
        lookup[x].append(pair)
        lookup[y].append(pair)


by_length = defaultdict(list)
best = 0
for pair in lookup[0]:
    already = {pair}
    y = pair[1] if pair[1] != 0 else pair[0]
    best = max(0, dfs(y, already, y))

longest = max(by_length)
print(best)
print(max(by_length[longest]))
