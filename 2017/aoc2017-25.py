import os
import re
from collections import defaultdict

beginR = re.compile(r'Begin in state ([A-Z])\.')
stepsR = re.compile(r'Perform a diagnostic checksum after (\d+) steps\.')
inStateR = re.compile(r'In state ([A-Z]):')
ifR = re.compile(r'If the current value is ([01]):')
writeR = re.compile(r'Write the value ([01])\.')
moveR = re.compile(r'Move one slot to the (left|right)\.')
continueR = re.compile(r'Continue with state ([A-Z])\.')

moves = {'left': -1, 'right': 1}

transition = {}
pos = 0
tape = defaultdict(lambda: 0)

with open(os.path.join('data', 'aoc25.txt')) as file:
    state = beginR.match(next(file)).group(1)
    steps = int(stepsR.match(next(file)).group(1))

    while next(file, None) is not None:
        this = inStateR.match(next(file)).group(1)
        for _ in range(2):
            read = int(ifR.search(next(file)).group(1))
            write = int(writeR.search(next(file)).group(1))
            move = moveR.search(next(file)).group(1)
            n_state = continueR.search(next(file)).group(1)

            transition[this, read] = (write, moves[move], n_state)

for _ in range(steps):
    write, move, n_state = transition[state, tape[pos]]
    tape[pos] = write
    pos += move
    state = n_state

result = sum(val for val in tape.values() if val == 1)
print(result)
