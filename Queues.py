
# FIFO Queue
from collections import deque

class Queue:
    #implementation of .__iter__() method and implementing .__len__()
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# from queues import Queue
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
print(len(fifo))

# printing the fifo queue
for element in fifo:
    print(element)

len(fifo)

print()

# LIFO Queue
# Building a Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# reverse order
lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element)

print()

# Different options when printing stack Queue
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())

print(lifo.pop())

print(lifo.pop())
        
