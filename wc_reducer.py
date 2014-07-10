#!/usr/bin/env python
import sys, re

def main():
    counts = {}
    for line in sys.stdin:
        word, c = line.split("\t")
        counts[word] = counts.get(word,0)+int(c)
    for word in counts:
        print "%s\t%d"%(word, counts[word])

if __name__=="__main__":
    main()
