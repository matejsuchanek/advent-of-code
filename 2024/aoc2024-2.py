import os


def satisfies(x, y, asc):
    return (x < y) is asc and 1 <= abs(y - x) <= 3


def is_safe(report):
    asc = report[0] < report[1]
    return all(
        map(lambda pair: satisfies(*pair, asc), zip(report, report[1:]))
    )


reports = []

safe = maybe_safe = 0

with open(os.path.join('data', 'aoc2.txt')) as file:
    for line in file:
        report = list(map(int, line.split()))
        reports.append(report)

        safe += is_safe(report)

print(safe)

for report in reports:
    if is_safe(report):
        maybe_safe += 1
    else:
        for i in range(len(report)):
            copy = report[:]
            copy.pop(i)
            if is_safe(copy):
                maybe_safe += 1
                break

print(maybe_safe)
