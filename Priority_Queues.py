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