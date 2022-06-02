# Depth First Search
# - Uses a stack

# LIFO

# Used for: Backtracking, complete search, exhausting possible paths

# Goes deep

# Time complexity: O( number of vertices + number of edges)
# Space complexity: O( number of vertices) - adding frames to the call stack due to recursive nature of the solution
# if you are traversing a balanced tree, then the space complexity is O(height of the tree)

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        # Append A and then go to A's children and append and go to the children of A's children and append recursive.
        for child in self.children:
            child.depthFirstSearch(array)
        return array


