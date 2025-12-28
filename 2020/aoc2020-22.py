import os

from collections import deque

cards1 = []
cards2 = []

with open(os.path.join('data', 'aoc22.txt')) as f:
    if next(f).startswith('Player 1:'):
        for line in f:
            line = line.rstrip()
            if not line:
                break
            card = int(line)
            cards1.append(card)

    if next(f).startswith('Player 2:'):
        for line in f:
            card = int(line.rstrip())
            cards2.append(card)

deck1, deck2 = deque(cards1), deque(cards2)

while deck1 and deck2:
    card1, card2 = deck1.popleft(), deck2.popleft()
    if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
    else:
        deck2.append(card2)
        deck2.append(card1)


def score(deck):
    score = multi = 0
    for card in reversed(deck):
        multi += 1
        score += multi * card
    return score


def new_game(deck1, deck2):
    configs = set()
    while deck1 and deck2:
        config = (','.join(map(str, deck1)), ','.join(map(str, deck2)))
        if config in configs:
            return 1, deck1, deck2
        configs.add(config)

        card1, card2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            first = deque(list(deck1)[:card1])
            second = deque(list(deck2)[:card2])
            winner, *_ = new_game(first, second)
            del first, second
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        elif winner == 2:
            deck2.append(card2)
            deck2.append(card1)

    player = 1 if deck1 else 2
    return player, deck1, deck2


print(score(deck1 or deck2))

deck1, deck2 = deque(cards1), deque(cards2)
winner, deck1, deck2 = new_game(deck1, deck2)

print(score(deck1 or deck2))
