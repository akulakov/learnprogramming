#!/usr/bin/env python
# Set card game
from random import shuffle

colors = ["red", "green", "blue"]
counts = range(1,4)
shapes = ["diamond", "squiggle", "oval"]
shades = ["blank", "filled", "hatched"]

deck = []
class Card:
    def __init__(self, col, cnt, shp, shd):
        self.col, self.cnt, self.shp, self.shd = col, cnt, shp, shd

    def __repr__(self):
        return "<%s %s %s %s>" % (self.col, self.cnt, self.shp, self.shd)

for col in colors:
    for cnt in counts:
        for shape in shapes:
            for shd in shades:
                deck.append(Card(col, cnt, shape, shd))

print("len(deck)", len(deck))
shuffle(deck)
cards, deck = deck[:12], deck[12:]
attrs = "col cnt shp shd".split()
for c in cards:
    print(c)

def is_set(cards):
    def same_or_diff(attr):
        vals = set(getattr(c,attr) for c in cards)
        return len(vals) in (1,3)
    return all(same_or_diff(a) for a in attrs)
