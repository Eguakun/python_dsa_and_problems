# subtree root index of the current subtree that were trying to create
# starts at 0,
# when we have these recurisve calls were trying to create one node at a time, the first one is our root node, but
# we cant create root node until we create the rest of the nodes so from the root node
# root idx = 0 when creating the left sub tree it will be equal to 1 bc thats the index of the subtree were now
# trying to create

# so on and so forth

# variables:
# root idx will be global
# lower --> node that were trying to create cannot be less than or equal to , start at negative inf
# upper --> node that were trying to create cannot be greater than or equal to , start at positive inf

# O(n) time
# O(n) space because we have to create output binary tree which has n nodes

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx # regular integer is immutable but this allows us to chage the value

def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    # base case 1 if theres no more elements, we finished creating tree
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    # if the value of the node that were trying to create is not within the lowere or upper bound range we need to return false
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, preOrderTraversalValues, currentSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)






