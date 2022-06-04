# InOrder Traverse:
# inorderTraverse(left)
# array.append(currentVal)
# inorderTraverse(right)

# PreOrder Traverse:
# array.append(currentVal)
# inorderTraverse(left)
# inorderTraverse(right)

# PostOrder Traverse:
# inorderTraverse(left)
# inorderTraverse(right)
# array.append(currentVal)


# Time complexity: O(n) for number of nodes
# Space complexity: O(n) for number of nodes,  array of length n
# O(d) if there was no array - frames on the call stack

def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)

    return array
