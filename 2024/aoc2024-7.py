import os

result = 0

with open(os.path.join('data', 'aoc7.txt')) as file:
    for line in file:
        goal, right = line.rstrip().split(': ')
        goal = int(goal)
        first, *values = [int(x) for x in right.split()]

        possible = {first}
        for val in values:
            possible = ({x * val for x in possible} |
                        {x + val for x in possible})
            possible = {x for x in possible if x <= goal}

        if goal in possible:
            result += goal

print(result)
