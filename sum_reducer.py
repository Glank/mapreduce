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
    total = 0
    for line in line_iter:
        if not line:
            continue
        total+=int(line)
    line_out.send_line('%d\n'%total)
    line_out.send_line('')

def main():
    reduce(SysLineIter(), SysLineOut())

if __name__=="__main__":
    main()
