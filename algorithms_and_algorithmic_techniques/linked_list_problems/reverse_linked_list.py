# Time complexity --> O(n) where n is the number of nodes
# Space complexity --> O(1)

def reverseLinkedList(head):
    p1, p2 = None, head # p2 is always the node that is in question
    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1

# why is p3 declared in the while loop instead of outside?
# - i want to handle this case cleanly without having to do a null check at the end and i want this loop to just work
# so im writing p3 as a brand new variable every iteration in the while loop. 