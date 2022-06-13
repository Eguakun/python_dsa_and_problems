# Time complexity: O(n)
# Space complexity: O(1)

def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree

    while currentNode is not None:
        # coming from top
        if previousNode is None or previousNode == currentNode.parent:
            # we have a left child to explore
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
                # coming back up from the left, so we now need to call callback on ourselves
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.right: # coming back up from right :
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode