#!/usr/bin/env python
import sys, re

def main():
    for line in sys.stdin:
        n = int(line.strip())
        print "%d\t%d"%(n/100000, 1)

if __name__=="__main__":
    main()
