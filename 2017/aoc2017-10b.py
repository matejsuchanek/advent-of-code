import os

from knot_hash import knot_hash

with open(os.path.join('data', 'aoc10.txt')) as file:
    print(knot_hash(next(file).rstrip()))
