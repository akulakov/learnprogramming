#!/usr/bin/env python

def sjoin(seq):
    # join sequence with spaces
    return ' '.join(str(x) for x in seq)

def cjoin(seq):
    # join sequence with commas
    return ', '.join(str(x) for x in seq)

def objrepr(*seq):
    return "<%s>" % cjoin(seq)
