# Iterative with a queue:

# Time complexity: O(n) where n is number of nodes in our tree because were exploring every node.
# swapping two  child nodes and adding to quque, constant time operations for every node

# Space complexity: O(n) because we have this queue and while the queue will never hold all of the n nodes of the tree at once,
# there will come a time where every single leaf node in the tree is in the queue
# In a perfectly balalnced BST you will n/2 leaf nodes. so space complexity converges to O(n) space


# recursive algorithm
# Breadth first search

# Start at the root node, swap its two children nodes,
# grab entire left subtree and swap with entire  right subtree
# do the same step to the next node on the next level.
# grab entire left subtree and swap with entire  right subtree
# keep doing until you get to leaf nodes with null children.
# Time complexity is O(n)
# Space complexity is O(d) where d is the depth of the tree and the depth is log(n) so also O(log(n))

# Iterative solution:
# O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        currentNode = queue.pop(0)
        if currentNode is None: # Null node
            continue
        swapLeftAndRight(currentNode)
        queue.append(currentNode.left)
        queue.append(currentNode.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


# Recursive Solution
# O(n) time | O(d) space - longest amount of frames on call stack being used up is going to amount to depth of the tree

def invertBinaryTreeRecursive(tree):
    if tree is None:
        return
    swapLeftAndRightRec(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRightRec(tree):
    tree.left, tree.right = tree.right, tree.left



