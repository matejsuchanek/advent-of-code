import os
from collections import defaultdict

def hash_word(s):
    cur = 0
    for x in s:
        cur = ((cur + ord(x)) * 17) % 256
    return cur    


prim = sec = 0
boxes = [list() for i in range(256)]

with open(os.path.join('data', 'aoc15.txt'), 'r') as file:
    for line in file:
        for s in line.split(','):
            prim += hash_word(s)

            if s.endswith('-'):
                label = s[:-1]
                box_i = hash_word(label)
                for i, (the_label, fl) in enumerate(boxes[box_i]):
                    if the_label == label:
                        boxes[box_i].pop(i)
                        break
            else:
                label, fl = s.split('=', 1)
                fl = int(fl)
                box_i = hash_word(label)
                for i, (the_label, _) in enumerate(boxes[box_i]):
                    if the_label == label:
                        boxes[box_i][i] = (label, fl)
                        break
                else:
                    boxes[box_i].append((label, fl))

for box_i, box in enumerate(boxes, start=1):
    sec += sum(box_i * i * fl for i, (_, fl) in enumerate(box, start=1))

print(prim)
print(sec)
