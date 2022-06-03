# O(n) time
# O(n) space


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindrome(head):
    isPalindromeResults = isPalindrome(head, head)
    return isPalindromeResults.outerNodesAreEqual

def isPalindrome(leftNode, rightNode):
    if rightNode is None:
        return LinkedListInfo(True, leftNode)
    recursiveCallResults = isPalindrome(leftNode, rightNode.next)
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual

    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
    nextLeftNodeToCompare = leftNodeToCompare.next

    return LinkedListInfo(recursiveIsEqual, nextLeftNodeToCompare)


class LinkedListInfo:
    def __init__(self, outerNodesAreEqual, leftNodeToCompare):
        self.outerNodesAreEqual = outerNodesAreEqual
        self.leftNodeToCompare = leftNodeToCompare


