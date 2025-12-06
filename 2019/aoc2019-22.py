deck = list(range(10007))
with open(os.path.join('data', 'aoc22.txt')) as file:
    for line in file:
        if line.strip() == 'deal into new stack':
            deck = deck[::-1]
        elif line.startswith('cut '):
            n = int(line[4:])
            deck = deck[n:] + deck[:n]
        elif line.startswith('deal with increment '):
            n = int(line[len('deal with increment '):])
            length = len(deck)
            new = [None] * length
            i = 0
            for c in deck:
                new[i] = c
                i = (i + n) % length
            deck = new

print(deck.index(2019))
