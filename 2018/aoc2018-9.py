import os
import re


class M:
    def __init__(self, i):
        self.i = i


regex = re.compile(r'(\d+) players; last marble is worth (\d+) points')

with open(os.path.join('data', 'aoc9.txt')) as file:
    match = regex.match(next(file))

players = int(match[1])

for coef in (1, 100):
    marble = int(match[2]) * coef

    score = [0] * players
    zero = M(0)
    cur = M(1)
    zero.next = zero.prev = cur
    cur.next = cur.prev = zero
    p = counter = 2
    while counter <= marble:
        if counter % 23 == 0:
            for i in range(7):
                cur = cur.prev
            score[p] += counter + cur.i
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            cur = cur.next
        else:
            cur = cur.next
            new = M(counter)
            new.next = cur.next
            new.prev = cur
            new.prev.next = new.next.prev = new
            cur = new
        counter += 1
        p = (p + 1) % players

    print(max(score))
