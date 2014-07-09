import sys, re

def main():
    for line in sys.stdin:
        for word in re.split('\W+',line):
            if word:
                print word+'\t1'

if __name__=="__main__":
    main()
