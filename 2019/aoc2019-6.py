import os
from collections import defaultdict, deque


def get_orbits(of):
    orbs = count = 0
    for p in chain[of]:
        o, c = get_orbits(p)
        orbs += o + c
        count += c + 1
    return orbs, count


chain = defaultdict(list)
graph = defaultdict(list)

with open(os.path.join('data', 'aoc6.txt')) as file:
    for line in file:
        l, r = line.strip().split(')')
        chain[l].append(r)
        graph[l].append(r)
        graph[r].append(l)

print(sum(get_orbits('COM')))

queue = deque()
start = graph['YOU'][0]
end = graph['SAN'][0]

queue.append(start)
dist = {start: 0}
while queue:
    node = queue.popleft()
    d = dist[node] + 1
    for n in graph[node]:
        if n not in dist:
            dist[n] = d
            if n == end:
                queue = None
                break
            queue.append(n)

print(dist[end])
