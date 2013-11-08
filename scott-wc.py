#!/usr/bin/python

import sys

def linecount(f):
    lines, words, chars = 0, 0, 0

    for l in f:
        lines += 1
        chars = chars + len(l)
        words = words + len(l.split())

    print lines, words, chars


if len(sys.argv) == 1:
    linecount(sys.stdin)
else: 
    filename = sys.argv[1]
    linecount(open(filename))



