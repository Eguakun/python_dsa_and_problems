from algorithms_and_algorithmic_techniques.helpers import get_a_list as g
# position of current node --> i
# position of child one --> 2i + 1
# position of child two --> 2i + 2

# Every parent node is less than it's children nodes.
# Min always at the root node.

# position of the parent node of a current node --> (i-1)//2

# Min Heap methods:
# - buildHeap() --> turns a list into a min heap representation
# - siftDown() --> move a node down to its appropriate place to maintain heap requirements
# - siftUp() --> move a node up to its appropriate place to maintain heap requirements
# - insert() --> insert a node/data into the heap
# - remove() --> remove a node/data from the heap, typically to retrieve the minimum value
# - swap() --> swap two nodes


# Time complexity of siftDown and siftUp
# both siftDown and siftUp runs in O(log(n)) where n is the number of values in the heap/binary tree
# because this is similar to binary search tree methods were essentially eliminating half the tree when we swap nodes.
# can do them in place so they don't take any space. same for insertion and removal

# Time complexity of buildHeap
# build heap runs in O(n) --> worst case
# start at first parent node and call sift down method and recursively do the same on each parent node until you get to the root node.
# the more nodes that we have in the heap, the more nodes we are having to call sift down for
# if you call sift down on a leaf node, no work has to be done. but on the higher level parent nodes, you sift them down at least one level.
# the higher up in teh heap you are the longer it takes sift down to run.


# Space complexity is O(1) because it all happens in place in the array, and we never allocate extra memory.

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for currentIdx in reversed(range(first_parent_idx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        child_one_idx = currentIdx * 2 + 1
        while child_one_idx <= endIdx: # don't want to call siftdown on node at the bottom of the heap. no where to sift it down
            child_two_idx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idxToSwap = child_two_idx
            else:
                idxToSwap = child_one_idx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                child_one_idx = currentIdx * 2 + 1
            else:
                return
    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]: # out of position, needs to swap  to maintain requirements
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop() # minimum
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    # O(1) time | O(1) space
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

l = g.generate_random_list(10)

m = MinHeap(l)


print(m.buildHeap(l))