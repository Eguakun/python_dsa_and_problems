# the new tail of the linked list is k positions behind the original tail
# position of new tail = len(linked_list) - k
# once we find the position of our new tail we can reiterate through the list
# restarting at the head, count the number of the positions to the new tail and at that point we have access to the
# new tail of our list.

# now we have access to the original head and original tail due to the first iteration

# and now on our second iteration, we have access to the new tail

# and we have access to the new head of the linked list because thats simply the new tail . next

# operations

# - make the original tail node point to the original  head node
# - set the new tail . next equal to our new head
# - then point the new tail to equal null since its the tail.

# time complexity: O(n) where n is the number of elements in our linked list
# space complexity: O(1)

# edge cases:
# 1- when k is equal to 0
    # - return 0
# 2- when k is a very large number
    # -shift linked list by this many position --> k mod len(linked list)
# 3- where k is equal to a negative number

# once we found the length of the linked list, were going to calcualte the position of the
# new tail based on the sign of k. If k is a negative integer, our forumla is going to be pnt = abs(k)

def shiftLinkedList(head, k):
    listLength = 1
    listTail = head

    if listTail is None:
        return None

    while listTail.next is not None:
        listTail = listTail.next
        listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
        return head

    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head

    for i in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead

