import os

grammar = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
scores = {
    ')': (3, 1),
    ']': (57, 2),
    '}': (1197, 3),
    '>': (25137, 4),
}

total = 0
ranking = []
with open(os.path.join('data', 'aoc10.txt'), 'r') as file:
    for line in file:
        line = line.rstrip()

        stack = []
        this = 0
        for c in line:
            if c in grammar:
                stack.append(c)
            elif grammar[stack.pop()] != c:
                this += scores[c][0]

        if this:
            total += this
        else:
            seq = []
            while stack:
                closing = grammar[stack.pop()]
                seq.append(closing)

            score = 0
            for c in seq:
                score = 5 * score + scores[c][1]
            ranking.append(score)

print(total)
ranking.sort()
print(ranking[len(ranking) // 2])
