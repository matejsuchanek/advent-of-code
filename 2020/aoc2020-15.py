init = [int(x) for x in input().split(',')]
turns = {y: x for x, y in enumerate(init)}

last = init[-1]
del turns[last]

for t in range(len(turns), 30000000-1):  # 2020-1
    if last not in turns:
        turns[last] = t
        last = 0
    else:
        tmp = t - turns[last]
        turns[last] = t
        last = tmp

print(last)
