def find_ancestors(root, target):
    if root == None:
        return False

    if root.val == target:
        return True

    if find_ancestors(root.left, target) or find_ancestors(root.right, target):
        return True
    else:
        return False

# Time complexity: O(n) where n is ndoes in the binary tree