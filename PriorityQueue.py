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

#Testing it
from queues import PriorityQueue
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# printing it
print(messages.dequeue()) 

print(messages.dequeue())

print(messages.dequeue())

print(messages.dequeue())

print()

# Handling Corner Cases in Your Priority Queue
from dataclasses import dataclass

@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

wipers < hazard_lights

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)
