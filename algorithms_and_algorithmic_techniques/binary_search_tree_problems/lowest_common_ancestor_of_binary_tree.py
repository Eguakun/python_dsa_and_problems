# start at the root because the root will alwasys be a common ancestor
# a number cant be the ancestor of another number if its in a different subtree

# if theres a split at the nodes where p and q are in different subtrees, where the split occurs
# is going to be the lowest common ancestor

# what if one of the nodes is equal to the root node. No node can be an ancestor of the root node, so
# you just return the root node.

# Time complexity: O(log n) because we only have to visit one node for every level in the tree.
# Space complexity: O(1)


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur