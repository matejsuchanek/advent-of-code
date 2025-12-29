import os
import re

def parse_line(line):
    groups = regex.fullmatch(line).groups()
    hour, minute, event = int(groups[0]), int(groups[1]), groups[2]
    g = None
    if event != 'falls asleep' and event != 'wakes up':
        g = int(regex2.fullmatch(event).group(1))
        if hour != 0:
            minute = 0
    return minute, g


with open(os.path.join('data', 'aoc4.txt')) as file:
    logs = sorted(map(str.strip, file))

regex = re.compile(r'\[\d+-\d+-\d+ (\d+):(\d+)\] (.+)')
regex2 = re.compile(r'Guard #(\d+) begins shift')

guards = {}
iterator = iter(logs)
new = lambda: next(iterator, None)
line = None
while True:
    if not line:
        line = new()
        if not line:
            break
    _, g = parse_line(line)
    next_line = new()
    if not next_line.endswith('falls asleep'):
        line = next_line
        continue
    sleep, _ = parse_line(next_line)
    awake, _ = parse_line(new())
    if g not in guards:
        guards[g] = [0 for x in range(60)]
    for m in range(60):
        if sleep <= m < awake:
            guards[g][m] += 1
        if m == awake:
            line = new()
            if line and line.endswith('falls asleep'):
                sleep, _ = parse_line(line)
                awake, _ = parse_line(new())
            else:
                break

# strategy 1
guard = top_minute = None
top = top_sleep = 0
for g, minutes in guards.items():
    my_sleep = sum(minutes)
    if my_sleep > top_sleep:
        top_sleep = my_sleep
        guard = g

for m, x in enumerate(guards[guard]):
    if x > top:
        top = x
        top_minute = m

print(top_minute * guard)

# strategy 2
guard = top_minute = None
top = 0
for g, minutes in guards.items():
    for m, x in enumerate(minutes):
        if x > top:
            top = x
            guard = g
            top_minute = m

print(top_minute * guard)
