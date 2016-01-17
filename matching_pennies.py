#!/usr/bin/env python
from random import randint, choice
from random import random

def matching_pennies():
    c1, c2 = randint(0,1), randint(0,1)
    print(c1, c2, "player %s wins" % (1 if c1==c2 else 2))
print("Matching Pennies")
matching_pennies()
print()

def rock_paper_scissors():
    m1, m2 = choice("rps"), choice("rps")
    if m1 == m2:
        print("draw")
    elif m1 + m2 in ("rs", "pr", "sp"):
        print("player 1 wins")
    else:
        print("player 2 wins")
print("Rock Paper Scissors")
rock_paper_scissors()
print()

def three_duel():
    players = [0.3, 0.6, 0.9]
    done = False
    while True:
        for n, p in enumerate(players):
            other = [x for x in range(len(players)) if x!=n]
            target = choice(other)
            if random() < p:
                print("%s %s removed by %s" % (target, players[target], p))
                del players[target]
                if len(players) == 1:
                    print("winner:", p)
                    done = True
                    break
            else:
                print("miss")
        if done:
            break
print("Three duel")
three_duel()
print()
