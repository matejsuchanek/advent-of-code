import os
import re
from collections import deque


class Node:

    def __init__(self, valve, tick=0, press=0, opened=None):
        self.valve = valve
        self.tick = tick
        self.press = press
        self.opened = opened or frozenset()

    def __repr__(self):
        return f'Node({self.valve!r}, {self.tick}, {self.press}, {self.opened})'

    @property
    def tuple(self):
        return (self.valve, self.opened), self.press

    def next(self):
        tick = self.tick + 1
        rel = sum(flows[v] for v in self.opened)
        press = self.press + rel
        if len(self.opened) == n_valves:
            yield Node(self.valve, tick, press, self.opened)
            return

        if self.valve not in self.opened and flows[self.valve] > 0:
            yield Node(self.valve, tick, press, self.opened | {self.valve})

        for v in graph[self.valve]:
            yield Node(v, tick, press, self.opened)


regex = re.compile(r'Valve ([A-Z]+) has flow rate=(\d+); '
                   'tunnels? leads? to valves? ((?:[A-Z]+(?:, |$))+)')

graph = {}
flows = {}

with open(os.path.join('data', 'aoc16.txt'), 'r') as file:
    for line in map(str.rstrip, file):
        match = regex.fullmatch(line)
        valve, flow, other = match.groups()
        flows[valve] = int(flow)
        graph[valve] = other.split(', ')

n_valves = len([v for v, n in flows.items() if n > 0])

start = Node('AA')
queue = [start]
already = {start.tuple[0]: start.tuple[1]}
for i in range(30):
    new = []
    for node in queue:
        for next_ in node.next():
            key, val = next_.tuple
            if already.get(key, -1) >= val:
                continue
            already[key] = val
            new.append(next_)
    queue = new

print(max(node.press for node in queue))
