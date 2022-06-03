# Time complexity: O(n)
# space complexity: O(d) where d is the depth of the tree
# if its a Balanced BST, the space copmlexity is O(log n)
# the pattern is:
# - for each node, the node to its left in the flattened list corresponds to the rightmost element in its left subtree
# - the node to its right in the flattened list corresponds to the leftmost element in its right subtree

# how do we get the leftmost node in the right subtree?
# how do we get the rightmost node in the left subtree?
# --->
# going to traverse this tree recursively, and when were at the root node,
# were going to want to get access to the rightmost node of the left subtree and connect it to the root node,
# and then somehow get access to the leftmost node in the right subtree, and connect it to the root node,
# in order to get access to them ,were going to have to traverse down the subtrees, make recursive calls and recursive calls
# are going to return to a given node the nodes that it has to connect to.

def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRighttMost

    return [leftMost, rightMost]

def connectNodes(left, right):
    left.right = right
    right.left = left
