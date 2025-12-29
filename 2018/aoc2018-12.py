import os


mapping = {}

with open(os.path.join('data', 'aoc12.txt')) as file:
    state = next(file).partition(': ')[2].strip()
    for line in map(str.strip, file):
        if line:
            f, to = line.split(' => ')
            mapping[f] = to

seen = {}

left = 0
epoch = 0
top = 50_000_000_000
while epoch < top:
    epoch += 1
    padded = state + '....'
    cur = '.....'
    out = ''
    for c in padded:
        cur = cur[1:] + c
        out += mapping.get(cur, '.')
    first = out.index('#')
    left += first - 2
    state = out[first:].rstrip('.')
    if epoch == 20:
        result = sum(i for i, p in enumerate(state, start=left) if p == '#')
        print(result)
    if state in seen:
        that_epoch, that_left = seen[state]
        diff_epoch = epoch - that_epoch
        remaining = top - epoch
        steps = remaining // diff_epoch
        left += (left - that_left) * steps
        epoch += steps * diff_epoch
    seen[state] = (epoch, left)

result = sum(i for i, p in enumerate(state, start=left) if p == '#')
print(result)
