import os

from collections import defaultdict

can_have = defaultdict(list)
sets = []
all_ingr = set()
allergens = {}

with open(os.path.join('data', 'aoc21.txt')) as f:
    for line in f:
        left, right = line.rstrip()[:-1].split(' (contains ')
        ingr = set(left.split(' '))
        all_ingr |= ingr
        sets.append(ingr)
        allerg = right.split(', ')
        for al in allerg:
            can_have[al].append(ingr)

while len(allergens) < len(can_have):
    for al, values in can_have.items():
        if al in allergens:
            continue
        inter = set.intersection(*values) - set(allergens.values())
        if len(inter) == 1:
            ing = inter.pop()
            allergens[al] = ing

total = 0
remain = all_ingr - set(allergens.values())
for s in sets:
    total += len(remain & s)
print(total)

print(','.join(allergens[key] for key in sorted(allergens)))
