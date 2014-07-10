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
        command, args = line.split('\t',1)
        if command=="test_factors":
            args = tuple(int(i) for i in args.split('\t'))
            n = args[2]
            for factor in test_factors(*args):
                line_out.send_line("factor\t%d\t%d\n"%(factor, n))
        else:
            line_out.send_line(line)
    line_out.send_line('')

def main():
    reduce(SysLineIter(), SysLineOut())

if __name__=="__main__":
    main()
