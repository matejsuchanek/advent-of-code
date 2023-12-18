class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.prev = None


def run(this, cups, rounds):
    mn, mx = min(cups), max(cups)
    for i in range(rounds):
        three_next = []
        x = this.next
        for _ in range(3):
            three_next.append(x)
            x = x.next
        lbs = {x.label for x in three_next}

        dst = this.label - 1
        while True:
            if dst < mn:
                dst = mx
            if dst not in lbs:
                break
            dst -= 1

        dest = cups[dst]

        this.next = three_next[2].next
        this.next.prev = this
        three_next[2].next = dest.next
        three_next[2].next.prev = three_next[2]
        dest.next = three_next[0]
        dest.next.prev = dest

        this = this.next


def init(labels, cups):
    last = first = None
    for label in labels:
        cup = Cup(label)
        cups[label] = cup
        if not first:
            first = cup
        if last:
            last.next = cup
            cup.prev = last
        last = cup

    last.next = first
    first.prev = last
    return first


input_ = input()
cups = {}
first = init([int(c) for c in input_], cups)
run(first, cups, 100)

labels = []
this = cups[1].next
while this.label != 1:
    labels.append(this.label)
    this = this.next

print(''.join(map(str, labels)))

cups = {}
labels = [int(c) for c in input_]
labels.extend(range(max(labels) + 1, 1_000_001))
first = init(labels, cups)
del labels
run(first, cups, 10_000_000)
print(cups[1].next.label * cups[1].next.next.label)
