#!/usr/bin/env python
from random import randint, choice
from math import floor

def public_good():
    players = [5,5,5,5]
    pool = 0
    multiplier = 3
    for _ in range(10):
        for n, p in enumerate(players):
            val = randint(0,floor(p))
            players[n] -= val
            pool += val
        print("players", players, "pool", pool)
        pool *= multiplier
        share = floor(pool / len(players))
        pool -= share * len(players)
        players = [p+share for p in players]
        print("players", players, "pool", pool)
        print()

print("Public Good")
public_good()
print()
