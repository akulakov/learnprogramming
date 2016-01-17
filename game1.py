#!/usr/bin/env python

from helpers import sjoin, cjoin
from random import shuffle

card_types = [
              ("tax",1,1),      # tax everyone 2 coins => bank
              ("soldier",2,1),
              ("sergeant",3,1),
              ("captain",4,2),
              ("emperor",1,5),
              ("prince",1,1),   # prince takes 1/3rd of bank
              ]

class Card:
    def __init__(self, name, power=1, honor=1):
        self.name = name
        self.power, self.honor = power, honor

    def __repr__(self):
        return "<%s %s %s>" % (self.name, self.power, self.honor)

class Player:
    coins = 4
    out = False

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def __repr__(self):
        return cjoin(self.name, self.cards, self.coins)

    def get_card(self, name):
        for c in self.cards:
            if c.name == name:
                return c

    def score(self):
        return sum(c.honor for c in self.cards)


deck = [Card(*c) for c in card_types]
deck += [Card(*c) for c in card_types]
for _ in range(15):
    deck.append(Card(*randchoice(card_types)))
shuffle(deck)

def draw(lst, n):
    items, lst = lst[:n], lst[n:]
    return items

players = [Player('a', draw(deck,5)),
           Player('b', draw(deck,5)),
           Player('c', draw(deck,5))
           ]

class Play:
    bank = 25

    def play_prince(self, player, card):
        amt = round(self.bank / 3)
        self.bank -= amt
        player.coins += amt
        player.cards.remove(card)

    def play_tax(self, player, card):
        others = [p for p in players if p!=player]
        for p in others:
            p.coins -= 2
            if p.coins < 0:
                players.remove(p)

    def check_end(self):
        return len(players) == 1

    def go(self):
        for p in players:
            prince = p.get_card("prince")
            tax = p.get_card("tax")
            if prince:
                self.play_prince(p, prince)
            elif tax:
                self.play_tax()
