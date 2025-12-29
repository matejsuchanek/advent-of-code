import os
import re

def count_removed(match):
    global removed
    text = cancelR.sub('', match[1])
    removed += len(text)
    return ''


with open(os.path.join('data', 'aoc9.txt')) as file:
    line = next(file)

garbR = re.compile(r'<((?:[^>]|(?<!!)(?:!!)*!>)*(?<!!)(?:!!)*)>')
cancelR = re.compile(r'(?<!!)(!!)*(!.)')

removed = 0
n = 1
while n:
    line, n = garbR.subn(count_removed, line)

level = 0
total = 0
for c in line:
    if c == '{':
        level += 1
        total += level
    elif c == '}':
        level -= 1

print(total)
print(removed)
