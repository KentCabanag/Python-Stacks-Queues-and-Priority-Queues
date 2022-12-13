# Representing Priority Queues With a Heap
# Using heapq.heappush()
from heapq import heappush

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits) # Testing the heappush

# Using heapq.heappop()
from heapq import heappop

heappop(fruits)

print(fruits)

# Python’s tuple comparison
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)# Printing if it is True or False

print(person2 < person3)# Printing if it is True or False

# Building a Priority Queue Data Type
# Basic priority queue implementation
# Using enqueue_with_priority() method
from heapq import heappop, heappush

class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

