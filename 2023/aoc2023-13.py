import os

row_patterns = []

with open(os.path.join('data', 'aoc13.txt'), 'r') as file:
    acc = []
    row_patterns.append(acc)
    for line in file:
        row = line.rstrip()
        if row:
            acc.append(row)
        else:
            acc = []
            row_patterns.append(acc)

transposed = []
for pattern in row_patterns:
    transposed.append(list(zip(*pattern)))

for err in (0, 1):
    total = 0
    for patterns, coef in [
        (row_patterns, 100),
        (transposed, 1),
    ]:
        for pattern in patterns:
            length = len(pattern)
            above = None
            for i in range(length-1):
                up_to = min(i+1, length-i-1)
                the_err = 0
                for x in range(up_to):
                    the_err += sum(a != b for a, b in zip(pattern[i-x], pattern[i+x+1]))
                if the_err == err:
                    above = i + 1
                    break
            if above is not None:
                total += coef * above

    print(total)
