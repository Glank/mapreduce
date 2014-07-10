#!/usr/bin/env python
import sys, re

def main():
    for line in sys.stdin:
        words = re.split("\W+", line)
        for word in words:
            if len(word)!=0:
                print word+"\t1"

if __name__=="__main__":
    main()
