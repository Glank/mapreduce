from subprocess import Popen,PIPE
import sys

def main():
    pcount = int(sys.argv[1])
    processes = [Popen(sys.argv[2:],stdout=PIPE) for p in xrange(pcount)]
    i = 0
    for line in sys.stdin:
        processes[i].stdin.write(line)
        processes[i].stdin.write("\n")
        i = (i+1)%pcount

if __name__=="__main__":
    main()
