import os
from collections import defaultdict

def wrong_pos(update):
    already = set()
    for i, num in enumerate(update):
        if needs[num] & already:
            return i
        already.add(num)

    return None


needs = defaultdict(set)
correct = wrong = 0

with open(os.path.join('data', 'aoc5.txt')) as file:
    for line in file:
        if line.strip() == '':
            break
        pre, post = line.rstrip().split('|')
        needs[pre].add(post)

    for line in file:
        update = line.rstrip().split(',')
        pos = wrong_pos(update)
        if pos is None:
            correct += int(update[len(update) // 2])
            continue

        while pos is not None:
            already = set(update[:pos])
            num = update[pos]
            first = min(update.index(x) for x in (needs[num] & already))
            update.insert(first, update.pop(pos))
            pos = wrong_pos(update)

        wrong += int(update[len(update) // 2])

print(correct)
print(wrong)
