import os


def make_group(num):
    result = set()
    stack = [num]
    while stack:
        index = stack.pop()
        result.add(index)
        stack.extend(x for x in data[index] if x not in result)
    return result


data = {}

with open(os.path.join('data', 'aoc12.txt')) as file:
    for line in map(str.rstrip, file):
        left, _, right = line.partition(' <-> ')
        my_id = int(left)
        others = list(map(int, right.split(', ')))
        data[my_id] = others

print(len(make_group(0)))

groups = 0
done = set()
for i in range(2000):
    if i in done:
        continue
    done |= make_group(i)
    groups += 1
print(groups)
