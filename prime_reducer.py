#!/usr/bin/env python
import sys

def SysLineIter():
    for line in sys.stdin:
        yield line

class SysLineOut:
    def send_line(self, line):
        if line:
            print line,

def test_factors(start, group_size, n):
    for i in xrange(start, start+group_size):
        if n%i==0:
            yield i

def reduce(line_iter, line_out):
    total = 0
    for line in line_iter:
        if not line:
            continue
        key, value = line.split('\t',1)
        start = int(key.split(':')[1])
        group_size, n = value.split('\t')
        group_size, n = int(group_size), int(n)
        for factor in test_factors(start, group_size, n):
            line_out.send_line("%d-%d\t%d\n"%(start,start+group_size,factor))
    line_out.send_line('')

def main():
    reduce(SysLineIter(), SysLineOut())

if __name__=="__main__":
    main()
