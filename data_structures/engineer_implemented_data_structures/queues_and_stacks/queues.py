# A Queue is a first in first out data structure.
# Enqueue is to add item to the end of the line
# Dequeue is to remove an item from the front of the line.
# Enqueue on one end and Dequeue from the other end.
# Just like a line at mcdonalds
# Best implementation for a queue in python is the deque data structure from the python collections module
# Use append() to enqueue and item, and popleft() to dequeue an item.
# The left is the front of the line and the right is the back of the line
# Data enters the deque to wait from the right and is served first to exit from the left
# Double ended queue = dequeue

from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(6)
my_queue.append(7)
print(my_queue)
print(my_queue.popleft())

