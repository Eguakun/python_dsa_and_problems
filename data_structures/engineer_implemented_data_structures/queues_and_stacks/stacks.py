# A stack is a last in first out data structure (LIFO)
# All push and pop operations are to/from the top of the stack.
# Push means to add data on top of the stack.
# Pop means to remove data from the top of the stack.
# Peek means to retrieve an item from the top of the stack without removing it.
# Clear means to delete all items from the stack.
# Stacks can be implemented with a list or a linked list
# Use append() to push an item onto the stack
# Use pop() to remove an item from the top of the stack.


# List implementation
# The 'top' of the stack for a list is the rightmost element.

# push data to the stack
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(11)
my_stack.append(19)
print(my_stack)

# pop data from the stack
print(my_stack.pop())
print(my_stack.pop())


# Stack using a wrapper class

class Stack:

    # constructor, we are going to make our stack a list, so
    # we can make use of the list methods that help implement the stack functionality

    def __init__(self):
        self.stack = list()

    # we will use the list append method to implement a push method to add data to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # we will need a pop method to implement the pop method to remove data from the top of the stack
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


# Test code for stack wrapper class

mystack = Stack()
mystack.push(4)
mystack.push(3)

print(mystack.peek())
print(mystack.__str__())
print(mystack.pop())





