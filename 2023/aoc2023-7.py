import os
from collections import defaultdict

sortkey_hand = {
    (5,): 1,
    (4, 1): 2,
    (3, 2): 3,
    (3, 1, 1): 4,
    (2, 2, 1): 5,
    (2, 1, 1, 1): 6,
    (1, 1, 1, 1, 1): 7,
}
sortkey_card = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
}

hands = []

with open(os.path.join('data', 'aoc7.txt'), 'r') as file:
    for line in file:
        hand, bid = line.split(maxsplit=1)
        bid = int(bid)

        mapping = defaultdict(lambda: 0)
        ordering = []
        for c in hand:
            mapping[c] += 1
            ordering.append(sortkey_card[c])

        by_count = tuple(sorted(mapping.values(), reverse=True))
        hands.append((sortkey_hand[by_count], tuple(ordering), bid))

hands.sort(reverse=True)

out = 0
coef = 0
for _, _, bid in hands:
    coef += 1
    out += coef * bid

print(out)
