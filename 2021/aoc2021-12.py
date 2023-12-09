from collections import defaultdict
import os


def dfs(node, already):
    out = 0
    for n in graph[node]:
        if n in already:
            continue
        if n == 'end':
            out += 1
            continue

        add = (n.lower() == n)
        if add:
            already.add(n)
        out += dfs(n, already)
        if add:
            already.remove(n)

    return out


graph = defaultdict(list)
with open(os.path.join('data', 'aoc12.txt'), 'r') as file:
    for line in file:
        a, b = line.rstrip().split('-')
        graph[a].append(b)
        graph[b].append(a)

out = dfs('start', {'start'})
print(out)
