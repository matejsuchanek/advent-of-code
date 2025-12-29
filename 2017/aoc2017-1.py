import os

with open(os.path.join('data', 'aoc1.txt')) as file:
    string = next(file).rstrip()

length = len(string)
result = 0
for i, c in enumerate(string, start=1):
    if i == length:
        next_c = string[0]
    else:
        next_c = string[i]
    if c == next_c:
        result += int(c)
print(result)

result = 0
for i, c in enumerate(string):
    next_index = (i + length // 2) % length
    if c == string[next_index]:
        result += int(c)
print(result)
