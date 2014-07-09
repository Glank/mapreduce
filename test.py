import os
import time

def run_test(name, func):
    print name 
    start = time.time()
    func()
    end = time.time()
    print "Delta:",end-start

def splitter_test(n):
    command = "cat nums.dat | python sum_mapper.py | python splitter.py %d hard_reducer reduce | python sum_reducer.py"
    command%=n
    os.system(command)

def stand_test():
    command = "cat nums.dat | python sum_mapper.py | python hard_reducer.py > /dev/null"
    os.system(command)

for i in xrange(1,6):
    run_test("%d processors..."%i, lambda:splitter_test(i))
