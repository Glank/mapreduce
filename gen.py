import random
import sys

n = 1000 if len(sys.argv)<2 else int(sys.argv[1])
for i in xrange(n):
    print random.randint(0,999999)
