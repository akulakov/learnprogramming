#!/usr/bin/env python

from random import choice, randint
from helpers import cjoin

colors = "red cyan green white black".split()
tokens = []

for c in colors:
    tokens.append(c)
tokens.extend(["gold"]*5)
    

class Card:
    def __init__(self, color, cost, points):
        self.color, self.cost, self.points = color, cost, points

    def __repr__(self):
        return objrepr(self.color, self.cost, self.points)

levels = [
         # deck: cost, points
         0: (4, 0),
         1: (7, 2),
         2: (9, 4),
         3: (11, 6),
         ]

decks = []
for n in range(4):
    deck = []
    for m in range(15):
        color = choice(colors)
        cost_n = randint(1, n+3)
        points = randint(1*(n+1), n*2)
        cost = []
        total = 0
        shuffle(colors)

        for _ in range(4):
            c = choice(colors)
            x = randint(0, n+1)
            if x:
                cost.append((c,x))
                total += x
                if total >= levels[n][0]:
                    break

        deck.append(Card(color, cost, levels[n][1]))
    decks.append(deck)


class Player:
    def __init__(self, name, cards):
        self.name, self.cards = name, cards

    def __repr__(self):
        return "%s %s" % (self.name, cjoin(cards))
