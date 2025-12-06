from collections import deque

chain = {}
graph = {}

def get_orbits(of):
    orbs = count = 0
    for p in chain.get(of, []):
        o, c = get_orbits(p)
        orbs += o + c
        count += c + 1
    return orbs, count

with open(os.path.join('data', 'aoc6.txt')) as file:
    for line in file:
        l, r = line.strip().split(')')
        chain.setdefault(l, []).append(r)
        graph.setdefault(l, []).append(r)
        graph.setdefault(r, []).append(l)

print(sum(get_orbits('COM')))

queue = deque()
start = graph['YOU'][0]
end = graph['SAN'][0]

queue.append(start)
dist = {start: 0}
while queue:
    node = queue.popleft()
    d = dist[node] + 1
    for n in graph.get(node, []):
        if n not in dist:
            dist[n] = d
            if n == end:
                queue = None
                break
            queue.append(n)

print(dist[end])
