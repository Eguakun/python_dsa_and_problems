# we want to be able to loop form back to the front.
# but its not doubly linked.
# what were going to do is reverse half of the linked list so that we can loop through it backwards byt actually going forwards

# split the linked list into two halfs,
# reverse the second half of the linked list
# have a pointer at the beginning of the first half, and a pointer at teh beginning of the last half
# loop through comparing each node and if any node doesnt match return false
# if a node does match, move both pointers and do the same check.
# if you reach the point where the pointers cross eachother, your algorithm is done and you can return true

# Time complexity: O(n)
# space complexity : O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def linkedListPalindrome(head):
    slowNode = head
    fastNode = head

    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    reversedSecondHalfNode = reverseLinkedList(slowNode)
    firstHalfNode = head
    
    while reversedSecondHalfNode is not None:
        if reversedSecondHalfNode.value != firstHalfNode.value:
            return False
        reversedSecondHalfNode = reversedSecondHalfNode.next
        firstHalfNode = firstHalfNode.next

    return True


def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

