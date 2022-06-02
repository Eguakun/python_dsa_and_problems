# Average Time Complexity: O(log(n)) | O(log(n))
# Worst Case Time Complexity: O(n) | O(n)
# Recursive solution
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    # since this is recursive implementation, we need to set a base case where we will stop calling this method.
    if tree is None:
        return closest
    if abs(target-closest) > abs(target-tree.value):
        closest = tree.value
    # if target is less than the value in the tree then we only need to go down left subtree
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    # if target is more than the value in the tree then we only need to go down right subtree
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else: # if we have a value that is equal to our target value
        return closest
# a number can only be less than, more than, or equal to another number





# Iterative implementation
# Average Time Complexity: O(log(n)) time | O(1) space
# Worst Case Time Complexity: O(n) time | O(1) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):

    currentNode = tree
    while currentNode is not None:
        # calculate differences between closest/target vs currentNode/target, update closest
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value

        if target < currentNode.value:
            currentNode = currentNode.left

        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
