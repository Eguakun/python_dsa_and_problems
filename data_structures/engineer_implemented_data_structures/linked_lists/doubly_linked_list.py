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

# Advantages of a Doubly Linked List over a Singly Linked List:
# - Can iterate through the list in either direction
# - Can delete a node without iterating through the list (if given a pointer to the node)

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return (' (' + str(self.data) + ') ')


class DoublyLinkedList:

    def __init__(self, r=None):
        self.root = r
        self.last = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            elif this_node.next_node is None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:

                    #  Case 1: Delete a middle node
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node

                        # Case #2: Delete the Last Node
                    else:  # delete last node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node

                        # Case #3: Delete the root node
                else:  # delete root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1

                return True  # data removed

            else:
                this_node = this_node.next_node # keep iterating through
        return False  # data not found

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()



# Doubly Linked List Test Code

doubly_linked_list = DoublyLinkedList()
for i in [5, 9, 3, 8, 9]:
    doubly_linked_list.add(i)

print("size = " + str(doubly_linked_list.size))
doubly_linked_list.print_list()
doubly_linked_list.remove(8)
print("size = " + str(doubly_linked_list.size))

print(doubly_linked_list.remove(15))
print(doubly_linked_list.find(15))
doubly_linked_list.add(21)
doubly_linked_list.add(22)
doubly_linked_list.remove(5)
doubly_linked_list.print_list()
print(doubly_linked_list.last.prev_node)

