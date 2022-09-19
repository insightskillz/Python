from queue import Queue
from threading import Thread
import copy

def producer(out_q):
    while True:
        out_q.put(copy.deepcopy(data))


def comsumer(in_q):
    whlie True:
        data = in_q.get()
        
