# Max Heap - list implementation
# What is a max heap? --> complete binary tree --> Every node <= its parent
# So the max is at the top
# These are great for retrieiving the maximum or minumum number in a fast way anytime that we need to
# Max heaps are fast. Insert into a max heap at O(log n) time complexity
# Get Max from a max heap in O(1) time complexity
# Remove max from a max heap in O(log n)

# with an unsorted list, you would have to sort to get the max, which is much slower

# you can get the parent of a node by diving the index of the node by 2.
# that will retrieve the index of the parent of the node
# parent(i) = i / 2

# you can get the left child of a parent node by multiplying the parent node's index by 2.
# that will retrieve the index of the left child node.
# left(i) = i * 2


# you can get the right child of a parent node by multiplying the parent node's index by 2 and adding 1.
# that will retrieve the index of the right child node.
# right(i) = i * 2 + 1

# Max heap operations
# push (insert)
# peek (get max)
# pop (remove max)


# a heap is ordered with the max as the first element and then left to right going down 1 level at a time.


# A MaxHeap always bubbles the highest value to the top, so it can be removed instantly.
# public functions: push, peek, pop
# private functions: swap, _floatUp, _bubbleDown, _str


class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap =[0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        # add value to end of array
        # float it up to its proper position
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        # return the value at heap[1]
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        # move max to the end of the array
        # delete it
        # bubble down the item at index 1 to its proper position
        # return max
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left_child = index * 2
        right_child = index * 2 + 1
        largest = index

        if len(self.heap) > left_child and self.heap[largest] < self.heap[left_child]:
            largest = left_child

        if len(self.heap) > right_child and self.heap[largest] < self.heap[right_child]:
            largest = right_child

        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)



    def __str__(self):
        return str(self.heap)


# MaxHeap test code

m = MaxHeap([95,3,21])
m.push(10)
print(m)
print(m.pop())
print(m.peek())
print(m)



