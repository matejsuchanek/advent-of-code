import os

scores = [3, 7]

one, two = 0, 1

with open(os.path.join('data', 'aoc14.txt')) as file:
    seq = next(file).rstrip()

rounds = int(seq)
seq = [int(x) for x in seq]
length = len(seq)
atleast = rounds + 10

before = None
while len(scores) < atleast or not before:
    first = scores[one]
    second = scores[two]
    combo = first + second
    if combo > 9:
        x, y = divmod(combo, 10)
        scores.append(x)
        if not before and scores[-length:] == seq:
            before = len(scores) - length
        scores.append(y)
    else:
        scores.append(combo)
    if not before and scores[-length:] == seq:
        before = len(scores) - length
    one = (one + first + 1) % len(scores)
    two = (two + second + 1) % len(scores)

print(''.join(str(x) for x in scores[rounds:atleast]))
print(before)
