#!/usr/bin/env python
from random import randint, random

def auction(players, start=0, step=1):
    print("players", players)
    x = start   # x is current price
    highest_bidder = None

    while True:
        print("highest_bidder", highest_bidder, '; x', x)
        if all(p<x for p in players):
            return None
        for n, p in enumerate(players):
            if highest_bidder == n:
                return n, x
            if p > x and randint(0,1):
                if random() > 0.85:
                    x = randint(x, p)
                else:
                    x += step
                highest_bidder = n

# print(auction([10,11,12,13]))

# 0: get 100, 1: get out of jail, 
chance_cards = range(5)

# 0: jail, 1: go to jail, 2: income tax,
tile_types = range(5)

class Property:
    house = hotel = False

    def __init__(self, name, price, base_rent):
        self.name, self.price = name, price
        self.rent = base_rent

blank = ' '
board = [[] for _ in range(70)]
class Player:
    coins = 1500
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

def display(board):
    lst = [' ' if not t else str(t[-1]) for t in board]
    return '|' + ''.join(lst) + '|'

players = [Player('a'), Player('b'), Player('c')]
board[0] = players
print(display(board))
