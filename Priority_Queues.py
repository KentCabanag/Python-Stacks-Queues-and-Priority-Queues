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