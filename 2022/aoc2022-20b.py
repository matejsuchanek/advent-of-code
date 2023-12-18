import os

class Entry:

    def __init__(self, value):
        self.value = value
        self.next = self.prev = None

    def __repr__(self):
        return f'Entry({self.value})'


nums = []

key = 811_589_153

with open(os.path.join('data', 'aoc20.txt'), 'r') as file:
    for line in file:
        nums.append(Entry(int(line.rstrip()) * key))
        if nums[-1].value == 0:
            zero = nums[-1]

length = len(nums)
for a, b in zip(nums[:-1], nums[1:]):
    a.next = b
    b.prev = a

nums[-1].next = nums[0]
nums[0].prev = nums[-1]

for _ in range(10):
    for entry in nums:
        steps = entry.value % (length - 1)

        if steps > 0:
            new = entry
            for i in range(steps):
                new = new.next

            entry.prev.next = entry.next
            entry.next.prev = entry.prev

            entry.next = new.next
            entry.next.prev = entry
            entry.prev = new
            entry.prev.next = entry

cur = zero
prim = 0
for _ in range(3):
    for _ in range(1000):
        cur = cur.next
    prim += cur.value

print(prim)
