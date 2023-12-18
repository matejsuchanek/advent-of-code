import os

def loop_for(public):
    x = 1
    loop = 0
    while x != public:
        loop += 1
        x = (x * 7) % 20201227
    return loop


with open(os.path.join('data', 'aoc25.txt')) as f:
    card = int(next(f).rstrip())
    door = int(next(f).rstrip())

card_loop = loop_for(card)
door_loop = loop_for(door)

x = 1
for i in range(door_loop):
    x = (x * card) % 20201227
print(x)
