# Heap is an array representation of a complete binary tree where each node is less than or equal to its children.
# Max heap: parent is greater than children

# No need to implement a node class for heap. We can use a list to represent a heap.

# heapq is priority queue in python

import heapq

# create a heap O(n)

array = [2, 1, 4, 0, 3, 6]
heapq.heapify(array)

print(array) # [0, 1, 4, 2, 3, 6]

heapq.heappush(array, 1)
heapq.heappop(array, 3)

print(array) # [1, 2, 4, 6, 3]

# insert / delete O(log n)

# heapify O(n)
