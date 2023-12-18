import os
from collections import defaultdict

inside = defaultdict(list)
contains = defaultdict(list)

with open(os.path.join('data', 'aoc7.txt')) as f:
    for line in f:
        line = line.rstrip()[:-1]
        bag, _, others = line.partition(' bags contain ')
        if others != 'no other bags':
            for other in others.split(', '):
                num, _, color = other.partition(' ')
                color = color.rpartition(' ')[0]
                inside[color].append(bag)
                contains[bag].append((int(num), color))

bags = set(inside['shiny gold'])

while True:
    new_bags = set()
    for b in bags:
        new_bags.update(inside[b])
    length = len(bags)
    bags |= new_bags
    new_length = len(bags)
    if length == new_length:
        break
print(length)


def count_for(bag):
    out = 0
    for num, other in contains[bag]:
        out += num * (1 + count_for(other))
    return out


print(count_for('shiny gold'))
