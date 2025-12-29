import os


class Cart:

    def __init__(self, pos, facing):
        self.pos = pos
        self.facing = facing
        self.active = True
        self._counter = 0
        self.history = [pos]

    def turn_left(self):
        self.facing = (-self.facing[1], self.facing[0])

    def turn_right(self):
        self.facing = (self.facing[1], -self.facing[0])

    def move(self):
        self.pos = (self.pos[0] + self.facing[0],
                    self.pos[1] + self.facing[1])
        self.history.append(self.pos)

    def intersect(self):
        if cart._counter == 0:
            self.turn_left()
            cart._counter = 1
        elif cart._counter == 1:
            cart._counter = 2
        elif cart._counter == 2:
            self.turn_right()
            cart._counter = 0


grid = []
pos_to_cart = {}
c_to_facing = {
    'v': (+1, 0),
    '^': (-1, 0),
    '<': (0, -1),
    '>': (0, +1),
}
facing_to_c = {f: c for c, f in c_to_facing.items()}

with open(os.path.join('data', 'aoc13.txt')) as file:
    for i, line in enumerate(map(str.rstrip, file)):
        grid.append(line)
        for j, c in enumerate(line):
            if c in c_to_facing:
                pos = (i, j)
                pos_to_cart[pos] = Cart(pos, c_to_facing[c])

first = True
while len(pos_to_cart) > 1:
    for pos, cart in sorted(pos_to_cart.items()):
        if not cart.active:
            continue

        row, col = pos
        c = grid[row][col]
        if c in c_to_facing:
            cart.facing = c_to_facing[c]
        elif c == '+':
            cart.intersect()
        elif c == '/':
            fc = facing_to_c[cart.facing]
            if fc in ('<', '>'):
                cart.turn_left()
            elif fc in ('^', 'v'):
                cart.turn_right()
        elif c == '\\':
            fc = facing_to_c[cart.facing]
            if fc in ('<', '>'):
                cart.turn_right()
            elif fc in ('^', 'v'):
                cart.turn_left()

        pos_to_cart.pop(cart.pos)
        cart.move()

        if cart.pos not in pos_to_cart:
            pos_to_cart[cart.pos] = cart
        else:
            other = pos_to_cart.pop(cart.pos)
            cart.active = False
            other.active = False
            if first:
                print(f'{cart.pos[1]},{cart.pos[0]}')
                first = False
                exit()

