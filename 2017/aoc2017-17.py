class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

steps = int(input())
cap = 2017

start = Node(0)
cur = start.next = Node(1)
cur.next = start

for val in range(2, cap + 1):
    for _ in range(steps):
        cur = cur.next
    tmp = cur.next
    new = cur.next = Node(val)
    new.next = tmp

print(new.next.value)
