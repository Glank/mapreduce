import sys

def main():
    word_counts = {}
    for line in sys.stdin:
        word,count = line.split('\t',1)
        word_counts[word] = word_counts.get(word,0)+int(count)
    for item in word_counts.items():
        print '%s\t%d'%item

if __name__=="__main__":
    main()
