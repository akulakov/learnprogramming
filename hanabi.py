#!/usr/bin/env python
# hanabi game
from random import shuffle

class Card:
    def __init__(self, val, col):
        self.val, self.col = val, col

    def __repr__(self):
        return "<%s %s>" % (self.col, self.val)

colors = "red green blue orange white".split()
deck = []
discarded = []
players = [[],[],[]]

for x in range(1,4):
    for c in colors:
        for _ in range(3):
            deck.append(Card(x,c))
for c in colors:
    deck.append(Card(5,c))
shuffle(deck)

for p in players:
    cards, deck = deck[:5], deck[5:]
    p.extend(cards)

fireworks = {c:[] for c in colors}


class Hanabi:
    bomb = 3
    hints = 8
    box_hints = 0

    def validate(self, card):
        fw = fireworks[card.col]
        if fw:
            return fw[-1].val == card.val-1
        else:
            return card.val == 1

    def make_move(self, player, card):
        if self.validate(card):
            fireworks[card.col].append(card)
            if card.val == 5:
                self.restore_hint()
        else:
            self.bomb -= 1
            if self.bomb==0:
                self.lose()
            discarded.append(card)
        player.remove(card)
        if deck:
            player.append(deck.pop())

    def display(self):
        for col, fw in fireworks.items():
            print(col, fw[-1] if fw else '')
        print("score:", sum( (fw[-1].val if fw else 0) for fw in fireworks.values() ))
        print("bomb", self.bomb)
        print()

    def discard(self, player, card):
        discarded.append(card)
        player.remove(card)
        if deck:
            player.append(deck.pop())

    def restore_hint(self):
        "Return hint token from box."
        if self.box_hints > 0:
            self.hints += 1
            self.box_hints -= 1

    def hint(self, p1, p2, val):
        assert p1 != p2
        print("%s cards:" % val, end='')
        for n, card in enumerate(p2):
            if val in (card.col, card.val):
                print(' ', n, card, end=',')
        print()
        self.hints -= 1
        self.box_hints += 1

    def lost_check(self):
        return not self.bomb

    def end_of_game(self):
        return not deck and not any(p for p in players)


class Player:
    def __init__(self, cards):
        self.cards = cards

hanabi = Hanabi()
print("player decks")
for p in players:
    print(p)

print()
print("init display, make moves with '1' cards")
hanabi.display()
for p in players:
    for c in p:
        if c.val == 1:
            hanabi.make_move(p, c)
            break

print("display again and player 1 makes move with first card and then discards new first card")
hanabi.display()
p=players[0]
hanabi.make_move(p, p[0])
hanabi.discard(p, p[0])

print("Hint for player 2, '1' cards")
hanabi.hint(players[0], players[1], 1)
print()

print("discarded", discarded)
print ("player 1", p)

print('end?', hanabi.end_of_game())
print("lost?", hanabi.lost_check())
