import os


def trees(right, down):
    trees = 0
    index = 0
    for line in lines[down::down]:
        index = (index + right) % len(line)
        trees += line[index] == '#'
    return trees


lines = []
with open(os.path.join('data', 'aoc3.txt')) as f:
    for line in f:
        lines.append(line.rstrip())

first = trees(3, 1)
print(first)
print(trees(1, 1) * first * trees(5, 1) * trees(7, 1) * trees(1, 2))
