import os

reward = {'rock': 1, 'paper': 2, 'scissors': 3}
mapping = {
    'A': 'rock',
    'X': 'rock',
    'Y': 'paper',
    'B': 'paper',
    'C': 'scissors',
    'Z': 'scissors',
}
defeats = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors',
}

total = 0
with open(os.path.join('data', 'aoc2.txt'), 'r') as file:
    for line in file:
        them, me = [mapping[x] for x in line.split()]
        total += reward[me]
        if me == them:
            total += 3
        elif defeats[them] == me:
            total += 6

print(total)

total = 0
with open(os.path.join('data', 'aoc2.txt'), 'r') as file:
    for line in file:
        them, result = line.split()
        them = mapping[them]
        if result == 'X':
            me = [x for x, val in defeats.items() if val == them].pop()
        elif result == 'Y':
            me = them
            total += 3
        elif result == 'Z':
            me = defeats[them]
            total += 6

        total += reward[me]

print(total)
