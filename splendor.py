#!/usr/bin/env python

import random
from random import randint
from random import choice as randchoice
from helpers import cjoin, objrepr, sjoin

colors = "red cyan green white black".split()
tokens = []

for c in colors:
    tokens.append(c)
tokens.extend(["gold"]*5)
    

class Card:
    def __init__(self, color, cost, points):
        self.color, self.cost, self.points = color, cost, points

    def __repr__(self):
        cost = ''.join(["%s%s" % (c[0][0], c[1]) for c in self.cost])
        return objrepr(self.color, self.points, cost)

levels = {
         # deck: cost, points
         0: (4, 0),
         1: (7, 2),
         2: (9, 4),
         3: (11, 6),
         }

def gen_sample(target_sums):
    """Generate random sample where sum of the sample matches at least one value in `target_sums`."""
    ssum = points = None
    # sample_list = [0]*6 + [1]*4 + [2]*3 + [3]*2 + [4]
    while ssum not in target_sums:
        points = random.sample(range(5), len(colors))
        ssum = sum(points)
    return points

decks = []
for n in range(4):
    deck = []
    for m in range(15):
        cost = gen_sample(4+n*2)
        # cost = []
        deck.append(Card(color, cost, levels[n][1]))
    decks.append(deck)


class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def __repr__(self):
        return "%s %s" % (self.name, cjoin(self.cards))

p1, p2 = Player('a'), Player('b')
for deck in decks:
    print(deck)
    print()
