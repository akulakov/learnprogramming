#!/usr/bin/env python

from random import randint
n = 20

def main():
    coins = 200
    avg = coins / n
    dist = []
    for x in range(n):
        amt = randint(0, round(avg*2))
        amt = min(amt, coins)   # can't give more than remaining coins
        if x == n-1:            # last pirate
            amt = coins
        dist.append(amt)
        coins -= amt

    print("dist", dist)
    print("sum(dist)", sum(dist))

main()
