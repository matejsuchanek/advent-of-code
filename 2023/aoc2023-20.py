import os
from collections import defaultdict, deque
from enum import IntEnum
from tqdm import tqdm


class Pulse(IntEnum):
    LOW = 1
    HIGH = 2


class Module:

    def __init__(self, outputs):
        self.outputs = outputs

    def register(self, name):
        pass

    def handle(self, pulse, prev):
        return None


class Broadcaster(Module):

    def handle(self, pulse, prev):
        return pulse


class FlipFlop(Module):

    def __init__(self, *args):
        super().__init__(*args)
        self.on = False

    def handle(self, pulse, prev):
        if pulse == Pulse.LOW:
            if not self.on:
                self.on = True
                return Pulse.HIGH
            else:
                self.on = False
                return Pulse.LOW

        return None


class Conjunction(Module):

    def __init__(self, *args):
        super().__init__(*args)
        self.inputs = {}

    def register(self, name):
        self.inputs[name] = Pulse.LOW

    def handle(self, pulse, prev):
        self.inputs[prev] = pulse
        if all(p == Pulse.HIGH for p in self.inputs.values()):
            return Pulse.LOW
        else:
            return Pulse.HIGH


modules = defaultdict(lambda: Module([]))

with open(os.path.join('data', 'aoc20.txt')) as file:
    for line in file:
        source, targets = line.rstrip().split(' -> ', 1)
        targets = targets.split(', ')
        if source.startswith('%'):
            name = source[1:]
            modules[name] = FlipFlop(targets)
        elif source.startswith('&'):
            name = source[1:]
            modules[name] = Conjunction(targets)
        elif source == 'broadcaster':
            modules[source] = Broadcaster(targets)

names = list(modules.keys())
for name in names:
    for tgt in modules[name].outputs:
        modules[tgt].register(name)

counts = [None, 0, 0]
i = 0
stop = False
tbar = tqdm()
while not stop:
    i += 1
    queue = deque()
    queue.append(('broadcaster', Pulse.LOW, ''))
    counts[Pulse.LOW] += 1
    while queue:
        mod, pulse, prev = queue.popleft()
        out = modules[mod].handle(pulse, prev)
        if out:
            for next_ in modules[mod].outputs:
                queue.append((next_, out, mod))
                counts[out] += 1
                if next_ == 'rx' and out == Pulse.LOW:
                    stop = True
                    print(i)

    if i == 1000:
        print(counts[1] * counts[2])
    tbar.update()
