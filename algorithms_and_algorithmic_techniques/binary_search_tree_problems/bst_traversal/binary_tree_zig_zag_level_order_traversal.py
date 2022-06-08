'''

             1
           /   \
         /      \
        2        3
      /  \     /  \
    /     5   6    \
   4                7



'''
'''
Naive initial thought:

One way to do this is to go level by level, ,which is a level order traversal of a binary tree
and for every even level we just reverse the list we add to our final resulting list. 

Better way:

[1]
[3,2]
[4,5,6,7]

Is there a way that we can relate each level to the level before it and see if there a pattern that we can find. 

So since we reverse directions each time we do a traversal of the tree, it may be good to use a stack since
stacks are really useful when trying to reverse something since its LIFO. 

So we can have two stacks.
stack_odd to hold my odd levels
stack_even to hold my even levels

So for each stack what im going to do is:
 pop off and if its in my odd stack, im going to add its left child then right child so when i pop off stack even, 
 i get a reading from right to left 
 
 and when i pop off stack even to go back to stack odd im going to add its right child then left child so i
 get a reading from left to right 

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        stack_odd = [root]
        stack_even = []
        level = []
        result = []

        while stack_odd or stack_even:
            while stack_odd:
                root = stack_odd.pop()
                level.append(root.val)
                if root.left:
                    stack_even.append(root.left)
                if root.right:
                    stack_even.append(root.right)
            result.append(level)
            level = []
            while stack_even:
                root = stack_even.pop()
                level.append(root.val)
                if root.right:
                    stack_odd.append(root.right)
                if root.left:
                    stack_odd.append(root.left)
            if level != []:
                result.append(level)
                level = []
        return result
        
