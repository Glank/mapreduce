#!/usr/bin/env python
import sys
import hashlib

def SysLineIter():
    for line in sys.stdin:
        yield line

class SysLineOut:
    def send_line(self, line):
        if line:
            print line,

def reduce(line_iter, line_out):
    totals = {}
    for line in line_iter:
        if not line:
            continue
        key, value = line.split('\t', 1)
        totals[key] = totals.get(key, 0)+int(value)
    for key in totals:
        line_out.send_line('%s\t%d\n'%(key,totals[key]))
    line_out.send_line('')

def main():
    reduce(SysLineIter(), SysLineOut())

if __name__=="__main__":
    main()
