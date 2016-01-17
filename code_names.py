
import nouns
from random import choice, shuffle
from copy import copy

def write_list():
    shuffle(nouns.list)
    fp = open("list.txt", 'w')
    n = nouns.list[:25]
    words = copy(n)
    while n:
        n, line = n[5:], n[:5]
        fp.write("%-20s %-20s %-20s %-20s %s\n\n\n" % tuple(line))
    return words

def write_map(words):
    shuffle(words)
    team1 = words[:8]
    team2 = words[8:16]
    neutral = words[16:24]
    assassin = words[24]

    fp = open("map.txt", 'w')
    fp.write("TEAM 1\n")
    for w in team1: fp.write(w + '\n')

    fp.write("\n\nTEAM 2\n")
    for w in team2: fp.write(w + '\n')

    fp.write("\n\nNEUTRAL\n")
    for w in neutral: fp.write(w + '\n')

    fp.write("\n\nassassin: %s\n" % assassin)


def main():
    w = write_list()
    write_map(w)
main()
