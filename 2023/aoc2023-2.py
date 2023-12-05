import os
from collections import defaultdict

prim = sec = 0

with open(os.path.join('data', 'aoc2.txt'), 'r') as file:
    for line in file:
        game_txt, _, rounds_txt = line.rstrip().partition(': ')
        game = int(game_txt.split(' ')[-1])

        bag = defaultdict(lambda: 0)
        for hand_txt in rounds_txt.split('; '):
            for pair in hand_txt.split(', '):
                n, color = pair.split(' ', 1)
                bag[color] = max(bag[color], int(n))

        if bag['red'] <= 12 and bag['green'] <= 13 and bag['blue'] <= 14:
            prim += game

        sec += bag['red'] * bag['green'] * bag['blue']

print(prim)
print(sec)
