import os
from collections import defaultdict

prim = 0

copies = defaultdict(lambda: 0)

with open(os.path.join('data', 'aoc4.txt'), 'r') as file:
    for line in file:
        card, _, txt = line.rstrip().partition(': ')
        card_n = int(card.split()[-1])
        copies[card_n] += 1

        win, _, numbers = txt.partition(' | ')
        win = {int(n) for n in win.split()}

        matched = sum(int(n) in win for n in numbers.split())
        if matched:
            prim += pow(2, matched - 1)
            for i in range(matched):
                copies[card_n + i + 1] += copies[card_n]

print(prim)
print(sum(copies.values()))
