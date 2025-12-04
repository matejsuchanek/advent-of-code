import os

dist = similarity = 0
left = []
right = []

with open(os.path.join('data', 'aoc1.txt')) as file:
    for line in file:
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)

left.sort()
right.sort()

for x, y in zip(left, right):
    dist += abs(y - x)

print(dist)

for x in left:
    similarity += x * right.count(x)

print(similarity)
