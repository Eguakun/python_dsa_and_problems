# Every linked list has nodes
# Every node has 2 parts: Data and pointer to the next node.
# Linked lists are helpful when you need data in a list but
# don't have memory capabilities for the data to be adjacent in memory

# That's why you must have data and a pointer because
# you may have to point to the specified given space in memory allocated for that peice of data

# Attributes of a linked list:
# - root or head: pointer to the beginning of the list
# - size - number of nodes in the list

# Operations of a linked list:
# - find(data)
# - add(data)
# - remove(data)
# - print_list()

# How to code a linked list in python:

# Node class:

# Node class has a constructor that sets the data passed in and optionally
# It also has a str method to give a string representation for printing
# Note that prev_node is only used for Doubly Linked Lists

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n

    def __str__(self):
        return (' (' + str(self.data) + ') ')

class LinkedList:

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: # data is not in the root node
                    prev_node.next_node = this_node.next_node
                else: # data is in the root node
                    self.root = this_node.next_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False # data not found

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node
        print('None')


# Linked List Test Code

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()

print("size = " +str(myList.size))
myList.remove(8)
print("size = " +str(myList.size))
print(myList.find(5))
print(myList.root)




