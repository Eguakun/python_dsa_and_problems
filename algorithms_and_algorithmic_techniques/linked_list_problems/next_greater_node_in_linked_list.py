'''
While iterating, we increment position

Since 4 is first value, we push the position and value to the stack item
NExt we go to next item. its a 3 which is less than 4, we enter it to the stack
NExt we go to 2. it is less than 3, add it to the stack
NExt we get to 5, it is greater than 2. We pop and check if the other iitems on the stack are greater than or less
if greater than we return the greater number as the next larger node, if not we return the 5

'''


class Solution:
    def nextLargerNodes(self, head):
        position = -1
        ans, stack = [], []

        while head:
            position += 1
            ans.append(0)

            while stack and stack[-1][1] < head.val:
                idx, value = stack.pop()
                ans[idx] = head.val

            stack.append((position, head.val))
            head = head.next
        return ans