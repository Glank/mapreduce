import sys
import os
import time

def print_usage():
    print """
    Usage:
        python test.py <kind>
    Where <kind> is either 'sum' or 'prime'
    """

def run_test(name, func):
    print name 
    start = time.time()
    func()
    end = time.time()
    print "Delta:",end-start

def splitter_test(n, kind):
    if kind=="sum":
        in_command = "cat nums.dat"
    else:
        in_command = 'echo "93479373729748721"'
    command = "%s | python %s_mapper.py | python splitter.py %d %s_reducer reduce"
    command%= (in_command, kind, n, kind)
    print command
    os.system(command)

def main():
    kind = sys.argv[1]
    for i in xrange(1,6):
        run_test("%d processors..."%i, lambda:splitter_test(i, kind))

if __name__=="__main__":
    try:
        main()
    except Exception():
        print_usage()
