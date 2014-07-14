#!/usr/bin/env python
import sys
from math import sqrt

def main():
    group_size = 100000
    for line in sys.stdin:
        n = int(line.strip())
        for i in xrange(2,int(sqrt(n))+1,group_size):
            print "test_factors:%d\t%d\t%d"%(i,group_size,n)

if __name__=="__main__":
    main()
