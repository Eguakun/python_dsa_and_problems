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

# A circular linked list is almost identical to a singly linked list except
# in a circular linked list, instead of the last node having a pointer to None,
# it will have a pointer back to the root node.

# when you add data to a circular linked list you add it in as the data next to the root node.
# you make the root node point to the new data and the new data point to what the root node was pointing to.

# Advantage for a circular linked list over a singly linked list is it is ideal for modeling continous looping objects.
# such as monopoly board or a race track

from singly_linked_list import LinkedList

class Node:

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return (' (' + str(self.data) + ') ')

class CircularLinkedList:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):
        this_node = self.root
        while True:
            if this_node.data ==d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:  # data is found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False  # data is not found
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()

# Circular Linked List Test Code

circular_linked_list = CircularLinkedList()
for i in [5,7,3,8,9]:
    circular_linked_list.add(i)
print("first print statement")
print("size = " + str(circular_linked_list.size))
print("first print statement")

print("second print statement")
print(circular_linked_list.find(8))
print("second print statement")

print("third print statement")
print(circular_linked_list.find(12))
print("third print statement")

print("loop print statement")
my_node = circular_linked_list.root
print(my_node, end="->")
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end="->")
print()
print("loop print statement")



print("Print list fuction ")

circular_linked_list.print_list()
print("Print list fuction ")






