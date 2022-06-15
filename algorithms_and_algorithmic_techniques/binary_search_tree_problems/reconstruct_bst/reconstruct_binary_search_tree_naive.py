# Naive Solution

# if were starting at node 10 then the first step is determine the right child
# when we find that the right child is 17 (since its the next biggest number in the list),
# then we know that the left child has to be between the value after 10 and the value before 17
# and in fact the entire left subtree of this binary search tree starting from 10 if to the left of 17
# and the right subtree of this binary search tree must be from 17 until the end of the list.
# then we iterate to the next value in our array and repeat this same process recursively


# example list = [10, 4, 2, 1, 5, 17, 19, 18]
# Time complexity: O(n ^2) because we have a recursive algorithm starting at the root node. to figure out what the right child is we have to loop through the array
# Space complexity: O(h) height of the tree due to h recursive calls on the call stack
# the actual space complexity is O(n) need to create output binary search tree

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    currentValue = preOrderTraversalValues[0]
    rightSubtreeRootIdx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubtreeRootIdx = idx
            break
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    rightSubtree = reconstructBst((preOrderTraversalValues[rightSubtreeRootIdx:]))
    return BST(currentValue, leftSubtree, rightSubtree)