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

print()

# Python’s tuple comparison
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)# Printing if it is True or False

print(person2 < person3)# Printing if it is True or False

print()

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

# from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue()) # Testing it
