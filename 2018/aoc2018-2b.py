import os

lines = []
with open(os.path.join('data', 'aoc2.txt')) as file:
    for line in map(str.strip, file):
        for other in lines:
            mistakes = 0
            for i, (a, b) in enumerate(zip(line, other)):
                if a != b:
                    mistakes += 1
                    pos = i
            if mistakes == 1:
                print(line[:pos] + line[pos+1:])
                exit(0)
        lines.append(line)
