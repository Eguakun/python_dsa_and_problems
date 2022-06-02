# Using a queue FIFO
# Instructions:

# Using a while loop
# 1. we pop the currentNode from the front of the queue,
# 2. we add the name of the currentNode to the final array
# 3. we add all of the currentNode's children nodes to the back of the queue
# 4. we pop the next node the from the front of the queue and assign it as the currentNode

# Time Complexity: O( number of vertices + number of edges)

# Space Complexity: O(v) where v is the number of vertices
# - storing an array of all of the nodes
# - queue data structure holds nodes but in worst case,
# - queue could hold all the nodes because all the children nodes are direct children of the root node
# - O(v - 1) which converges to O(v)


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        queue = [self]
        # while the queue is not empty
        while len(queue) > 0:
            # set current to be the node at the beginning of queue
            current = queue.pop(0)
            # append name to array
            array.append(current.name)
            # for every child append that child to back of the queue
            for child in current.children:
                queue.append(child)
            # once empty we will return the array
        return array
