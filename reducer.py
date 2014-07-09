import sys

def SysLineIter():
    for line in sys.stdin:
        yield line

class SysLineOut:
    def send_line(self, line):
        if line:
            print line,

def reduce(line_iter, line_out):
    word_counts = {}
    for line in line_iter:
        if not line.strip():
            continue
        try:
            word,count = line.split('\t',1)
            word_counts[word] = word_counts.get(word,0)+int(count)
        except:
            print "'%s'"%line
            exit()
    for w,c in word_counts.items():
        line_out.send_line('%s\t%d\n'%(w,c))
    line_out.send_line('')

def main():
    reduce(SysLineIter(), SysLineOut())

if __name__=="__main__":
    main()
