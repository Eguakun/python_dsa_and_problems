# Each piece of data in a tree is called a "node"
# Each connection between nodes is called an "edge"
# In a binary search tree, each node can have up to 2 child nodes
# Bottom nodes with no children are called "leaf nodes"
# top node with no parents is called the "root node".
# Two nodes with the same parent are called "sibling nodes".

# In a binary search tree, each node is greater than every node in its left subtree.
# Each node is less than every node in its right subtree

# Binary Search tree operations:
# - Insert
# - Find
# - Delete
# - Get_size
# - Traversals
    # - Pre order traversal
        # - Visits root before visiting the root's subtrees.
    # - In Order traversal --> Can deliver values in sorted order.
        # - Visits root between visiting the root's subtrees

# Advantages of binary search trees?
# - Because trees use recursion for most operations, they are fairly easy to implement.
# - Speed --> You can insert, delete, and find in O(height of the tree) = O(log n)

# Implementation Details:
# - Constructor sets three attributes: data, left subtree, and right subtree
# - Insert inserts a new subtree into the proper location
# - Find finds a value. If value not found, raise Data Not Found Exception.
# - Get_size returns the number fo nodes in the tree (excluding None nodes).
# - Preorder prints a preorder traversal of the tree
# - Inorder prints an inorder traversal of the tree
# - Duplicates are not allowed in a binary search tree

class Custom_Exceptions(Exception):
    def not_found_error(self):
        raise Exception("Data Not Found in this Binary Search Tree. Please try again.")
    def duplicate_value_error(self):
        raise Exception("Duplicate Value! Please Try Again")


custom_exceptions = Custom_Exceptions()

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            # return custom_exceptions.duplicate_value_error()  -->  duplicate value
            return False
        elif self.data > data:
        # if the root node is greater than the data we give, we need to move down the left subtree

            if self.left is not None:
                return self.left.insert(data) # recursive call to insert which will continue to do comparisons
            else:
                self.left = Tree(data) # once there is no more left subtree to go down, we have reached the bottom
                # insert the new subtree there and return true
                return True
        else:
        # if the root node is less than the data we give, we need to move down the right subtree

            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data) # once there is no more right subtree to go down, we have reached the bottom
                # insert the new subtree there and return true
                return True

    def find(self, data ):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is None:
                # return custom_exceptions.not_found_error()
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                # return custom_exceptions.not_found_error()
                return False
            else:
                return self.right.find(data)

    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data, end=" ")
            if self.right is not None:
                self.right.inorder()


# Binary Search Tree test code

tree = Tree(7)
tree.insert(9)

for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14]:
    tree.insert(i)

for i in range(16):
    print(tree.find(i), end=" ")
print('\n', tree.get_size())

tree.preorder()
print()
tree.inorder()
print()










