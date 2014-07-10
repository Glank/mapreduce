from multiprocessing import Process, Queue
from types import *
import sys
import io
import time
from importlib import import_module

def enqueue(queues):
    i = 0
    for line in sys.stdin:
        queues[i].put(line)
        i = (i+1)%len(queues)
    for q in queues:
        q.put('')

def output(queue,n):
    done_count = 0
    while done_count<n:
        result = queue.get()
        if result !='':
            print result,
        else:
            done_count+=1

class QueueLineOut:
    def __init__(self, queue):
        self.queue = queue
    def send_line(self, line):
        self.queue.put(line)

def QueueLineIter(queue):
    cont = True
    while cont:
        result = queue.get()
        if result !='':
            yield result
        else:
            cont = False

def main():
    n = int(sys.argv[1])
    module = __import__(sys.argv[2])
    target = getattr(module, sys.argv[3])
    in_queues = [Queue() for i in xrange(n)] 
    out_queue = Queue()
    processes = [
        Process(target=output, args=(out_queue,n))
    ]
    for queue in in_queues:
        process = Process(
            target=target,
            args=(QueueLineIter(queue), QueueLineOut(out_queue))
        )
        processes.append(process)
    for process in processes:
        process.start()    
    enqueue(in_queues)
    for process in processes:
        process.join()    

if __name__=="__main__":
    main()
