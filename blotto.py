#!/usr/bin/env python

# Blotto game: two players distribute an equal number over three slots, player
# who has higher number in most slots, wins

from random import randint
n = 8

def distribute(n, m):
    # this will not work well for some values of m and n: e.g. if avg is less than 0.25,
    # entire amount will always be in the last slot
    x = n
    slots = []
    avg = n / m
    for y in range(m):
        val = randint(0, round(avg*2))
        val = min(val, x)
        if y == m-1:
            val = x
        slots.append(val)
        x -= val
    return slots

def main():
    for x in range(15):
        play(distribute(n,3), distribute(n,3))

def play(lst1, lst2):
    print(lst1, lst2, end=' ')
    s1 = sum(lst1[n]>lst2[n] for n in range(3))
    s2 = sum(lst1[n]<lst2[n] for n in range(3))
    if s1==s2:
        print("draw")
    elif s1>s2:
        print("player 1 wins")
    else:
        print("player 2 wins")

main()
