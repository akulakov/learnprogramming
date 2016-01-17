#!/usr/bin/env python
from random import randint
# prisoner's dilemma; moves: 1=silent, 2=snitch
SILENT = 1
SNITCH = 2

def main():
    for _ in range(20):
        moves = [randint(SILENT, SNITCH), randint(SILENT, SNITCH)]      # players 1, 2
        calc(moves)

def calc(moves):
    p1, p2 = moves
    if p1 == p2 == SILENT:
        print("both 1 year sentence")
    elif p1 == p2 == SNITCH:
        print("both 2 year sentence")
    elif p1 == SILENT:
        print("player 1: 3 years, player 2: go free")
    elif p2 == SILENT:
        print("player 2: 3 years, player 1: go free")

main()
